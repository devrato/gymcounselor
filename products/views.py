from django.shortcuts import render

from services.models import Service


def prod_view(request, slug):
    user = request.user
    try:
        service = Service.objects.get(slug=slug)
    except:
        service = None
    allService = Service.objects.all()
    context = {
        'title': service.name,
        'product': service,
        'allService': allService,
        'users': user,

    }
    return render(request, 'products/product.html', context)
