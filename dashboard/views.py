from django.contrib.auth import login
from django.shortcuts import render, redirect

# from services.models import Service


def dash_view(request):
    # services = Service.objects.all()
    if request.user.is_authenticated:
        context_one = {
            'title': 'Dashboard',
            'user': request.user,
        }
    return render(request, 'dashboard/dash.html', context_one)
    # return redirect('/')
