from django.shortcuts import render

from .models import Service


def service_view(request):
    service = Service.objects.all()
    user = request.user

    context = {
        'title': 'Services',
        'users': user,
        'services': service,
    }
    return render(request, 'services/service.html', context)
