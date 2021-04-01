from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from .models import ExtendedUser


def login_view(request):
    valuenext = request.POST.get('next')
    comment = request.POST.get('comment')
    print(comment)
    if request.user.is_authenticated:
        return redirect('/product/PCOS')
    context = {
        'title': 'Login',
        'valuenext': valuenext,
    }

    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if valuenext != '':
                return redirect('/product/PCOS')
            else:
                return redirect('home')
        else:
            return render(request, "user/login.html", {"error": "Invalid Login Credentials."})
    else:
        return render(request, 'user/login.html', context)


def register_view(request):
    valuenext = request.POST.get('next')
    if request.user.is_authenticated:
        return redirect('/product/PCOS')
    context = {
        'title': 'Register',
        'valuenext': valuenext,
    }
    if request.method == "POST":
        password = request.POST.get('password')
        try:
            check_user = User.objects.get(
                username=request.POST['username'])
            if check_user is not None:
                return render(request, 'user/register.html', {'error': 'Email is already taken.'})
        except:
            # user = User.objects.create_user(username=request.POST['username'], password=password,
            #                                 email=request.POST['username'], first_name=request.POST['first_name'],
            #                                 last_name=request.POST['last_name'])
            user = User.objects.create_user(username=request.POST['username'], password=password,
                                            email=request.POST['username'])
            user.save()
            ExtendedUser(user=user).save()
            user = authenticate(request, username=request.POST.get(
                'username'), password=password)
            if user is not None:
                auth.login(request, user)
                if valuenext != '':
                    return redirect('/product/PCOS')
                else:
                    return redirect('home')
            else:
                return render(request, "user/login.html", {"error": "Invalid Login Credentials."})
        else:
            return render(request, 'user/login.html', context)

        # else:
        #     print("Password Not Matched")
        #     return render(request, 'user/register.html', {'error': 'Passwords dont match'})
    else:
        return render(request, 'user/register.html', context)
