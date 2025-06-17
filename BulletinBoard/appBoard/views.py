from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Post, Response, Category, Subscription
from .forms import PostForm, ResponseForm
from django.contrib import messages
from django.db.models import Q

def post_list(request):
    # Получаем последние 5 объявлений для отображения на главной странице
    latest_posts = Post.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()
    
    context = {
        'latest_posts': latest_posts,
        'categories': categories,
    }
    return render(request, 'board/post_list.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Объявление успешно создано')
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('board:post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Объявление успешно обновлено')
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    responses = post.response_set.all().order_by('-created_at')
    is_subscribed = False
    if request.user.is_authenticated:
        is_subscribed = Subscription.objects.filter(user=request.user, category=post.category).exists()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.post = post
            response.author = request.user
            response.save()
            
            # Отправка email автору объявления
            send_mail(
                'Новый отклик на ваше объявление',
                f'Пользователь {request.user.username} оставил отклик на ваше объявление "{post.title}"',
                settings.DEFAULT_FROM_EMAIL,
                [post.author.email],
                fail_silently=False,
            )
            messages.success(request, 'Ваш отклик успешно отправлен')
            return redirect('board:post_list')
    else:
        form = ResponseForm()
    return render(request, 'board/post_detail.html', {
        'post': post,
        'responses': responses,
        'form': form,
        'is_subscribed': is_subscribed
    })

@login_required
def my_responses(request):
    user_posts = Post.objects.filter(author=request.user)
    responses = Response.objects.filter(post__in=user_posts).select_related('post', 'author').order_by('-created_at')
    
    # Добавляем контент объявлений в контекст
    for response in responses:
        response.post_content = response.post.content
    
    return render(request, 'board/my_responses.html', {'responses': responses})

@login_required
def response_accept(request, pk):
    response = get_object_or_404(Response, pk=pk)
    if response.post.author != request.user:
        return redirect('board:profile')
    
    # Отправка email автору отклика
    send_mail(
        'Ваш отклик принят',
        f'Ваш отклик на объявление "{response.post.title}" был принят',
        settings.DEFAULT_FROM_EMAIL,
        [response.author.email],
        fail_silently=False,
    )
    
    response.delete()
    messages.success(request, 'Отклик успешно принят')
    return redirect('board:profile')

@login_required
def subscribe(request, category_code):
    if request.method == 'POST':
        category = get_object_or_404(Category, code=category_code)
        subscription, created = Subscription.objects.get_or_create(
            user=request.user,
            category=category
        )
        if created:
            messages.success(request, f'Вы успешно подписались на категорию {category.name}')
        else:
            messages.info(request, f'Вы уже подписаны на категорию {category.name}')
        return redirect('board:post_detail', pk=request.POST.get('post_id'))
    return redirect('board:post_list')

@login_required
def profile(request):
    # Получаем подписки пользователя
    subscriptions = Subscription.objects.filter(user=request.user).select_related('category')
    
    # Получаем объявления пользователя
    user_posts = Post.objects.filter(author=request.user).select_related('category')
    
    # Получаем отклики на объявления пользователя
    responses_to_posts = Response.objects.filter(post__author=request.user).select_related('post', 'author')
    
    # Получаем отклики пользователя на чужие объявления
    user_responses = Response.objects.filter(author=request.user).select_related('post')
    
    context = {
        'subscriptions': subscriptions,
        'user_posts': user_posts,
        'responses_to_posts': responses_to_posts,
        'user_responses': user_responses,
    }
    return render(request, 'board/profile.html', context)
