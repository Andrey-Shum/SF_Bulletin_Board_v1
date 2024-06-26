from django.db import models
from appAccounts.models import User


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('appBoard.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"Подписка {self.user.email}"
