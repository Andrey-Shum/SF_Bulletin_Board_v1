from django import forms
from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.conf import settings
import random

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        
        # Генерируем код подтверждения
        confirmation_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        user.confirmation_code = confirmation_code
        user.save()
        
        # Отправляем письмо с кодом подтверждения
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Ваш код подтверждения: {confirmation_code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
        
        return user 