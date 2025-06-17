from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Subscription
from appBoard.models import Post

@shared_task
def send_newsletters():
    """
    Задача для отправки ежедневных новостных рассылок.
    Отправляет подписчикам информацию о новых объявлениях в их категориях.
    """
    # Получаем все категории
    categories = dict(Post.category.field.choices)
    
    for category_code, category_name in categories.items():
        # Получаем подписчиков категории
        subscribers = Subscription.objects.filter(category=category_code)
        
        if not subscribers:
            continue
            
        # Получаем новые объявления за последние 24 часа
        yesterday = timezone.now() - timedelta(days=1)
        new_posts = Post.objects.filter(
            category=category_code,
            time_create__gte=yesterday,
            is_published=True
        )
        
        if not new_posts:
            continue
            
        # Формируем сообщение
        message = f"Новые объявления в категории '{category_name}' за последние 24 часа:\n\n"
        for post in new_posts:
            message += f"- {post.title}\n"
            message += f"  Автор: {post.author.username}\n"
            message += f"  Создано: {post.time_create.strftime('%d.%m.%Y %H:%M')}\n"
            message += f"  Ссылка: {settings.SITE_URL}/post/{post.pk}/\n\n"
        
        # Отправляем письма всем подписчикам
        for subscriber in subscribers:
            send_mail(
                subject=f'Новые объявления в категории {category_name}',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.user.email],
                fail_silently=False,
            ) 