from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Subscription
from appBoard.models import Post, Category

# Create your views here.

@login_required
def subscribe(request, category_code):
    category = get_object_or_404(Category, code=category_code)
    subscription, created = Subscription.objects.get_or_create(
        user=request.user,
        category=category.code
    )
    
    if created:
        messages.success(request, f'Вы успешно подписались на категорию {category.name}')
    else:
        messages.info(request, f'Вы уже подписаны на категорию {category.name}')
    
    return redirect('board:category', category_code=category.code)

@login_required
def unsubscribe(request, category_code):
    category = get_object_or_404(Category, code=category_code)
    subscription = get_object_or_404(Subscription, user=request.user, category=category.code)
    subscription.delete()
    messages.success(request, f'Вы отписались от категории {category.name}')
    return redirect('board:category', category_code=category.code)

@login_required
def my_subscriptions(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/my_subscriptions.html', {
        'subscriptions': subscriptions
    })

def send_newsletter(category):
    subscribers = Subscription.objects.filter(category=category)
    posts = Post.objects.filter(category=category, is_published=True).order_by('-time_create')[:5]
    
    if posts:
        message = f"Новые объявления в категории {category}:\n\n"
        for post in posts:
            message += f"- {post.title}\n"
        
        for subscriber in subscribers:
            send_mail(
                f'Новые объявления в категории {category}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [subscriber.user.email],
                fail_silently=False,
            )
