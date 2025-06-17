from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

# Create your views here.

@login_required
def confirm_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == request.user.confirmation_code:
            request.user.is_confirmed = True
            request.user.save()
            messages.success(request, 'Ваш email успешно подтвержден!')
            return redirect('post_list')
        else:
            messages.error(request, 'Неверный код подтверждения')
    return render(request, 'accounts/confirm_code.html')
