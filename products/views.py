from django.shortcuts import render
from django.core.mail import send_mail
import razorpay
from services.models import Service
from dashboard.models import Order
import random
from gym.settings import EMAIL_HOST_USER


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
        auth=('rzp_test_V2KMUMI2Ommcj1', 'YzemijL2imRE9yxKep1c0ydD'))
    payment = client.order.create({'amount': order_amount, 'currency': 'INR',
                                   'payment_capture': '1'})
    context = {
        'title': service.name,
        'product': service,
        'allService': allService,
        'users': user,
    }

    return render(request, 'products/product.html', context)


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
        message = 'The order id is - ' + order_id
        subject = 'Hey'
        to = ['joythegoodboy@gmail.com', 'sajal.deyasi@gymcounselor.com', 'sajal.deyasi8@gmail.com']
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            to,
            fail_silently=False,
        )
        return render(request, 'products/thank.html')
    else:
        service = Service.objects.all()
        context = {
            'title': 'Home',
            'users': request.user,
            'service': service,
        }
        return render(request, 'products/thank.html', {'context': context})


def trial(request, slug):
    user = request.user
    try:
        service = Service.objects.get(slug=slug)
    except:
        service = None
    allService = Service.objects.all()
    #
    # order_amount = 50000
    # order_currency = 'INR'
    # order_receipt = 'order_rcptid_11'
    # client = razorpay.Client(
    #     auth=('rzp_test_V2KMUMI2Ommcj1', 'YzemijL2imRE9yxKep1c0ydD'))
    # payment = client.order.create({'amount': order_amount, 'currency': 'INR',
    #                                'payment_capture': '1'})

    context = {
        'title': service,
        'product': service,
        'allService': allService,
        'users': user,
    }
    return render(request, 'products/blank.html', context)

# def pcosblank(request):
#     service = Service.objects.all()
#     context = {
#         'title': 'Home',
#         'users': request.user,
#         'service': service,
#     }
#     return render(request, 'products/blank.html', {'context': context})

# def order_successmodal(request):
#     if request.method == 'POST':

#         # data needed
#         razorpay_payment_id = request.POST['razorpay_payment_id']
#         customer_email = request.user.email

#         # order id generator
#         digits = "0123456789"
#         order_id = "GC" + random.choice(digits) + random.choice(
#             digits) + random.choice(digits) + random.choice(digits)

#         # previous order checker
#         is_duplicate_order_number = Order.objects.filter(
#             order_id=order_id).first()
#         while is_duplicate_order_number is not None:
#             order_id = "GC" + random.choice(digits) + random.choice(
#                 digits) + random.choice(digits) + random.choice(digits)
#             is_duplicate_order_number = Order.objects.filter(
#                 order_id=order_id).first()

#         orderdata = Order(order_id=order_id, razorpay_payment_id=razorpay_payment_id,
#                           service_name="PCOS", customer_email=customer_email)
#         orderdata.save()

#         service = Service.objects.all()
#         context = {
#             'title': 'Home',
#             'users': request.user,
#             'service': service,
#             'order_successmodal': 1
#         }
#         return render(request, 'products/thank.html', {'context': context})
#     else:
#         service = Service.objects.all()
#         context = {
#             'title': 'Home',
#             'users': request.user,
#             'service': service,
#             'order_successmodal': 0
#         }
#         return render(request, 'products/thank.html', {'context': context})
