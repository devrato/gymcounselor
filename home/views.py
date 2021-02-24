from django.http import JsonResponse
from django.shortcuts import render

from services.models import Service


def home_view(request):
    service = Service.objects.all()
    user = request.user

    context = {
        'title': 'home',
        'users': user,
        'service': service,
    }
    return render(request, 'home/home.html', context)


def about_view(request):
    service = Service.objects.all()
    user = request.user
    context = {
        'title': 'About',
        'users': user,
        'service': service,
    }
    return render(request, 'home/about.html', context)


def work_view(request):
    user = request.user
    context = {
        'title': 'Work',
        'users': user,
    }
    return render(request, 'home/work.html', context)


def contact_view(request):
    service = Service.objects.all()
    user = request.user
    context = {
        'title': 'Contact Us',
        'users': user,
        'service': service,
    }
    return render(request, 'home/contact.html', context)


def newsletter_subscribe_view(request):
    return JsonResponse(data={'message': 'Email Received', 'is_received': True}, status=200)
