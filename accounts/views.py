from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


# Create your views here.
@login_required(login_url='account-login')
def accountProfile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)

@unauthenticated_user
def accountLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Your username and/or password is not correct. Please try again.')

    context = {}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='account-login')
def accountRegister(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account for ' + user + ' created. Please sign in.')
            return redirect('account-login')
        else:
            errors = form.errors.as_data()
            for err in errors:
                if err == 'username':
                    messages.error(request, 'User with that username already exists. Please choose another username.')
                elif err == 'password2':
                    messages.error(request, 'Password and Password confirmation did not match. Please try again.')
                else:
                    messages.error(request, 'Something went wrong. Please check your input data and try again.')

            #messages.error(request, keys)
            #messages.error(request, 'User with that username already exists. Please choose another username.')


            

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def accountLogout(request):
    logout(request)
    return redirect('account-login')