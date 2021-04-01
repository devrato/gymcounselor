from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutHomeView.as_view(), name='workout_home'),
    path('post/<str:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    # path('filter/', views.BlogFilterView.as_view(), name='workout_filter'),
    # path('comment/add/<str:post_id>/', views.add_comment, name='add_comment'),
]
