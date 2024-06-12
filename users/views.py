# users/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def dashboard(request):
    user_role = request.user.user_role
    if user_role == 'superuser':
        return redirect('superuser_dashboard')
    elif user_role == 'moderator':
        return redirect('moderator_dashboard')
    elif user_role == 'employee':
        return redirect('employee_dashboard')

@login_required
def superuser_dashboard(request):
    return render(request, 'superuser_dashboard.html')

@login_required
def moderator_dashboard(request):
    return render(request, 'moderator_dashboard.html')

@login_required
def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard or any other page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
        else:
            print(form.errors)  # Print validation errors to console for debugging
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

