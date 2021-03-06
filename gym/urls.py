from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from services.views import service_view
from home.views import home_view, about_view, work_view, contact_view, newsletter_subscribe_view, landing_page_view
from account.views import login_view, register_view
from dashboard.views import dash_view, updateuserdetails
from products.views import prod_view, order_success
from html_to_pdf.views import GeneratePdf 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('work/', work_view, name='work'),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('services/', service_view, name='services'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dash_view, name='dashboard'),
    path('PCOS_Campaign/', landing_page_view, name='landing'),
    path('myorders/', dash_view, name='myorders'),
    path('product/<slug:slug>', prod_view, name='prod_detail'),
    # path('trial/<slug>', trial, name='trial'),
    path('ordersuccess', order_success, name='order_success'),
    # subscribe newsletter url
    path('subscribe-news-letter/', newsletter_subscribe_view, name='subscribe_letter'),
    # path('order_successmodal', order_successmodal, name='order_successmodal'),
    path('updateuserdetails', updateuserdetails, name='updateuserdetails'),
    url('social-auth/', include('social_django.urls', namespace='social')),
    # blog urls
    path('blog/', include('blog.urls')),
    #workout urls
    path('videos',include('workout.urls')),
    #html_top_pdf
    path('pdf/', GeneratePdf.as_view()), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
