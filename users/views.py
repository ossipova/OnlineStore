from django.shortcuts import render, redirect
from users.forms import AuthForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthForm
        }
        return render(request, 'users/auth.html', context=context)

    if request.method == 'POST':
        form = AuthForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'Try again :(')

                return render(request, 'users/auth.html', context={
                    'form': form
                })


def logout_view(request):
    logout(request)
    return redirect('/products')


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            password1, password2 = form.cleaned_data['password1'], form.cleaned_data['password2']
            if password1 == password2:
                User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=password1
                )
                return redirect('/user/login/')
            else:
                form.add_error('password1', 'password1 != password2')

                return render(request, 'users/register.html', context={'form': form})
