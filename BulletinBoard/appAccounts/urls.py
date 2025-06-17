from django.urls import path
from . import views

urlpatterns = [
    path('confirm-code/', views.confirm_code, name='confirm_code'),
] 