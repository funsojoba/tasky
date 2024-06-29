from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from rest_framework.views import APIView



from django.contrib.auth import authenticate, login, logout



def register(request):
    if request.method == 'POST':
        User = get_user_model()
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username, password=password, email=email)
        return render(request, 'authentication/login.html')
    return render(request, 'authentication/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = get_user_model().objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('tasks:task_list')
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid username or password'})

    return render(request, 'authentication/login.html')



