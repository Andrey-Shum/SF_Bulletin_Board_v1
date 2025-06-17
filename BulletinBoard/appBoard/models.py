from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from appAccounts.models import User


class Category(models.Model):
    """
    Модель категории

    neme - название категории
    Метод __str__ выводит название категории
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, unique=True, default='XX')
    description = models.TextField(default='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    """
    Модель объявления

    author - поле автора
    title - поле заголовка
    content - поле сообщения
    category - поле категории
    time_create - поле дата создания
    time_update - поле дата редактирования
    is_published - флаг публикации поста
    Метод __str__ выводит заголовок и автора
    verbose_name и verbose_name_plural для удобного чтения единственного имени
    модели (заменяет стандартное соглашение об именовании)
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    video = models.FileField(upload_to='post_videos/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Response(models.Model):
    """
    Модель отклика

    text - текст отклика
    author - автор
    post - пост
    created_at - время создания отклика
    метод __str__ возвращает строку, которая указывает,
    кто сделал отклик и на какое объявление, а также время создания отклика.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Response to {self.post.title} by {self.author.email}"


class Subscription(models.Model):
    """
    Модель подписки на категорию

    user - пользователь, который подписался
    category - категория, на которую подписался пользователь
    created_at - дата создания подписки
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_subscriptions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'category')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.user.username} подписан на {self.category.name}"
