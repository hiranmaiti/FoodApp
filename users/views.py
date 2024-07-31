from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

# def register(request):
#     form=UserCreationForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('login')
#     return render(request,'users/register.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')