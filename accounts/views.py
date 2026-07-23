from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import (
    EmployerLoginForm,
    EmployerRegistrationForm,
    JobSeekerLoginForm,
    JobSeekerRegistrationForm,
)
from .models import UserProfile


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = JobSeekerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to JobPortal.')
            return redirect('home')
    else:
        form = JobSeekerRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def employer_register(request):
    if request.user.is_authenticated:
        return redirect('employer_dashboard')

    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Employer account created successfully!')
            return redirect('employer_dashboard')
    else:
        form = EmployerRegistrationForm()

    return render(request, 'accounts/employer_register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = JobSeekerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile = getattr(user, 'profile', None)
            if profile and profile.is_employer:
                messages.error(request, 'Please use the Employer Login page.')
                return redirect('employer_login')
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    else:
        form = JobSeekerLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def employer_login(request):
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile and profile.is_employer:
            return redirect('employer_dashboard')
        return redirect('home')

    if request.method == 'POST':
        form = EmployerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile = getattr(user, 'profile', None)
            if not profile or not profile.is_employer:
                messages.error(request, 'This account is not registered as an employer.')
                return redirect('login')
            login(request, user)
            messages.success(request, f'Welcome, {profile.company_name or user.username}!')
            return redirect('employer_dashboard')
    else:
        form = EmployerLoginForm()

    return render(request, 'accounts/employer_login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
