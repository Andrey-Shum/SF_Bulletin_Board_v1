from django.db import models
from appAccounts.models import User


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2)

    def __str__(self):
        return f"Подписка {self.user.email} на категорию {self.category}"

    class Meta:
        unique_together = ('user', 'category')
