from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role='customer')
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')
