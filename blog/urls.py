from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='blog_home'),
    path('post/<str:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('filter/', views.BlogFilterView.as_view(), name='blog_filter'),
]
