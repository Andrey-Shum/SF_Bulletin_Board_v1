from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Расширяет встроенную в Django AbstractUser модель,
    добавляя дополнительные поля для
    кода подтверждения и Флаг подтверждения аккаунта.
    """
    confirmation_code = models.CharField(max_length=6, blank=True)
    is_confirmed = models.BooleanField(default=False)
