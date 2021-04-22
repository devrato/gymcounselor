from django.shortcuts import render, redirect
from django.core.mail import send_mail
import razorpay
from razorpay import Client

from services.models import Service
from products.models import Product, ProductDetail
from dashboard.models import Order
import random
from django.http import HttpResponse
from gym.settings import EMAIL_HOST_USER
from django_simple_coupons.validations import validate_coupon
from django_simple_coupons.models import Coupon


def prod_view(request, slug):
    if request.method == 'POST' and "Submit Coupon" in request.POST:
        user = request.user
        coupon_code = request.POST.get('Promo Code', '0')
        print(coupon_code)
        status = validate_coupon(coupon_code=coupon_code, user=user)
        if status['valid']:
            coupon = Coupon.objects.get(code=coupon_code)
            
            # coupon.use_coupon(user=user)
            try:
                service = Service.objects.get(slug=slug)
                products = Product.objects.filter(service=service).order_by('identity')
            except:
                service = None
            allService = Service.objects.all()
            data = {
                'amount': 50000,
                'currency': 'INR',
                'receipt': 'order_rcptid',
                'payment_capture': '1'
            }
            client = razorpay.Client(auth=('rzp_test_V2KMUMI2Ommcj1', 'YzemijL2imRE9yxKep1c0ydD'))
            payment = client.order.create(data=data)
            context = {
                'title': service.name,
                'product': service,
                'allService': allService,
                'users': user,
                'products': products,
            }
            val = int(request.session.get('value', default='0'))
            if request.user.is_authenticated:
                if val != 0:
                    try:
                        product_detail = ProductDetail.objects.filter(service=service).get(identity=val)
                        discount_value = int(coupon.get_discounted_value(initial_value=product_detail.price))
                    except:
                        product_detail = None
                    context['product_detail'] = product_detail
                    context['price'] = discount_value
                    context['value'] = val
                    context['coupon_code'] = coupon_code
            else:
                request.session['value'] = 0
            return render(request, 'products/product.html', context)

        return HttpResponse(status['message'])

    elif request.method == 'POST':
        request.session['value'] = int(request.POST.get('value', '0'))
        if request.user.is_authenticated:
            return redirect('/product/PCOS')
        else:
            return redirect('/register/?next=/product/PCOS')
    else:
        user = request.user
        try:
            service = Service.objects.get(slug=slug)
            products = Product.objects.filter(service=service).order_by('identity')
        except:
            service = None
        allService = Service.objects.all()
        data = {
            'amount': 50000,
            'currency': 'INR',
            'receipt': 'order_rcptid',
            'payment_capture': '1'
        }
        client: Client = razorpay.Client(auth=('rzp_test_V2KMUMI2Ommcj1', 'YzemijL2imRE9yxKep1c0ydD'))
        payment = client.order.create(data=data)
        context = {
            'title': service.name,
            'product': service,
            'allService': allService,
            'users': user,
            'products': products
        }
        val = int(request.session.get('value', default='0'))
        if request.user.is_authenticated:
            if val != 0:
                try:
                    product_detail = ProductDetail.objects.filter(service=service).get(identity=val)
                except:
                    product_detail = None
                context['product_detail'] = product_detail
                context['price'] = product_detail.price
                context['value'] = val
        else:
            request.session['value'] = 0
        return render(request, 'products/product.html', context)


def order_success(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('Coupon name')
        status = validate_coupon(coupon_code=coupon_code, user=request.user)
        print(status['valid'])
        if status['valid']:
            coupon = Coupon.objects.get(code=coupon_code)
            coupon.use_coupon(user=request.user)
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
        # message = 'The order id is - ' + order_id
        # subject = 'Hey'
        # to = ['joythegoodboy@gmail.com', 'sajal.deyasi@gymcounselor.com', 'sajal.deyasi8@gmail.com']
        # send_mail(
        #     subject,
        #     message,
        #     EMAIL_HOST_USER,
        #     to,
        #     fail_silently=False,
        # )
        return render(request, 'products/thank.html')
    else:
        service = Service.objects.all()
        context = {
            'title': 'Home',
            'users': request.user,
            'service': service,
        }
        return render(request, 'products/thank.html', {'context': context})

#
# def trial(request, slug):
#     user = request.user
#     try:
#         service = Service.objects.get(slug=slug)
#     except:
#         service = None
#     allService = Service.objects.all()
#     #
#     # order_amount = 50000
#     # order_currency = 'INR'
#     # order_receipt = 'order_rcptid_11'
#     # client = razorpay.Client(
#     #     auth=('rzp_test_V2KMUMI2Ommcj1', 'YzemijL2imRE9yxKep1c0ydD'))
#     # payment = client.order.create({'amount': order_amount, 'currency': 'INR',
#     #                                'payment_capture': '1'})
#
#     context = {
#         'title': service,
#         'product': service,
#         'allService': allService,
#         'users': user,
#     }
#     return render(request, 'products/blank.html', context)

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
