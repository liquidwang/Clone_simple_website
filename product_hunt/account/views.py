from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['re_password']

        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', {'user_name_error': 'The Username already exists.'})
        except User.DoesNotExist:
            if password1 == password2:
                User.objects.create_user(username=user_name, password=password1)
                return redirect('home')
            else:
                return render(request, 'signup.html', {'password_error': 'Passwords do not match.'})

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']

        user = auth.authenticate(username=user_name, password=pass_word)

        if user is None:
            return render(request, 'signin.html', {'error_message': 'The Username does Not exist or Wrong password.',
                                                   })
        else:
            auth.login(request, user)
            return redirect('home')

def log_out(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
