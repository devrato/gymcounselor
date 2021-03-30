#from django.contrib.auth import login
from django.shortcuts import render
from .models import Order
from account.models import ExtendedUser
from services.models import Service

def dash_view(request):
    if request.user.is_authenticated:
        service = Service.objects.all()
        orders = Order.objects.filter(customer_email=request.user.email)
        extended_user = ExtendedUser.objects.filter(user=request.user)
        props = {}
        # props['title'] = 'Dashboard'
        props['user'] = extended_user
        props['orders'] = orders
        props['services'] = service
        props['title'] = 'Hello'
        return render(request, 'dashboard/dash.html', {'props': props})

def updateuserdetails(request):
    if request.method == 'POST':
        service = Service.objects.all()
        user = request.user
        extended_user = ExtendedUser.objects.get(user=user)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        extended_user.ph_no = request.POST['ph_no']
        extended_user.weight = int(request.POST['weight'])
        extended_user.height = int(request.POST['height'])
        user.save()
        extended_user.save()
        print(extended_user)
        orders = Order.objects.filter(customer_email=request.user.email)
        extended_user = ExtendedUser.objects.filter(user=request.user)
        props = {}
        props['title'] = 'Dashboard'
        props['user'] = extended_user
        props['orders'] = orders
        props['services'] = service

        return render(request, 'dashboard/dash.html', {'props': props})
