from django.contrib import admin
from .models import Subscription


# Зарегистрируйте свои модели здесь.
@admin.register(Subscription)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'category')
    list_filter = ('category', )
    search_fields = ['user__username', 'category__name']
