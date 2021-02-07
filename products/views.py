from django.shortcuts import render
import razorpay
from services.models import Service
from dashboard.models import Order
import random


def prod_view(request, slug):
    user = request.user
    try:
        service = Service.objects.get(slug=slug)
    except:
        service = None
    allService = Service.objects.all()

    order_amount = 50000
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    client = razorpay.Client(
        auth=('rzp_test_2GM0584mxsjPdZ', '12MKr4OPhllSPwKBg3QLdzAl'))
    payment = client.order.create({'amount': order_amount, 'currency': 'INR',
                                   'payment_capture': '1'})

    context = {
        'title': service.name,
        'product': service,
        'allService': allService,
        'users': user,
    }
    return render(request, 'products/product.html', context)


# def order_success(request):
#     return render(request, 'products/thank.html')


def order_success(request):
    if request.method == 'POST':

        # data needed
        razorpay_payment_id = request.POST['razorpay_payment_id']
        customer_email = request.user.email

        # order id generator
        digits = "0123456789"
        order_id = "GC" + random.choice(digits) + random.choice(
            digits) + random.choice(digits) + random.choice(digits)

        # previous order checker
        is_duplicate_order_number = Order.objects.filter(
            order_id=order_id).first()
        while is_duplicate_order_number is not None:
            order_id = "GC" + random.choice(digits) + random.choice(
                digits) + random.choice(digits) + random.choice(digits)
            is_duplicate_order_number = Order.objects.filter(
                order_id=order_id).first()

        orderdata = Order(order_id=order_id, razorpay_payment_id=razorpay_payment_id,
                          service_name="PCOS", customer_email=customer_email)
        orderdata.save()

        service = Service.objects.all()
        context = {
            'title': 'Home',
            'users': request.user,
            'service': service,
            'order_success': 1
        }
        return render(request, 'home/home.html', {'context': context})
    else:
        service = Service.objects.all()
        context = {
            'title': 'Home',
            'users': request.user,
            'service': service,
            'order_success': 0
        }
        return render(request, 'home/home.html', {'context': context})
