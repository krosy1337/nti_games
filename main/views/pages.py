import random

from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect('user')
    return render(request, 'main/home.html')


def user(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'main/user.html', {'user': request.user, 'score': random.randint(0, 100)})


def page_not_found(request, exception):
    return render(request, 'main/error.html')
