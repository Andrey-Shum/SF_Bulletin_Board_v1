from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('subscribe/<str:category_code>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<str:category_code>/', views.unsubscribe, name='unsubscribe'),
    path('my-subscriptions/', views.my_subscriptions, name='my_subscriptions'),
] 