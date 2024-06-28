from django.db import models
from appAccounts.models import User


class Subscription(models.Model):
    """
    Модель подписки

    user - внешний ключ к модели User
    category - внешний ключ к модели Category из приложения appBoard.
    Метод __str__() возвращает строковое представление объекта Subscription,
    включающее email пользователя, для которого создана подписка.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'appBoard.Category',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Подписка {self.user.email}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
