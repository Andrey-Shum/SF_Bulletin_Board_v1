from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('my-responses/', views.my_responses, name='my_responses'),
    path('my-responses/<int:pk>/accept/', views.response_accept, name='response_accept'),
    path('category/<str:category_code>/subscribe/', views.subscribe, name='subscribe'),
    path('profile/', views.profile, name='profile'),
] 