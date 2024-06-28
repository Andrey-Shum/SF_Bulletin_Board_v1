from django.db import models
from ckeditor.fields import RichTextField
from appAccounts.models import User


class Category(models.Model):
    """
    Модель категории

    neme - название категории
    Метод __str__ выводит название категории
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=2, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


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
    title = models.CharField('Заголовок', max_length=255)
    content = RichTextField('Объявление', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


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

    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отклик от {self.author} на '{self.post.title}' в {self.created_at}"

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
