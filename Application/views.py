from django.shortcuts import render, redirect
from .models import UserRegister
from .forms import UserRegisterForm,LoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('dashboard')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.error(request, 'You have logged out successfully.')
    return redirect('dashboard')
 