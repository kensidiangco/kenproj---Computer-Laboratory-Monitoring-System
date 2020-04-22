from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('login', views.user_form, name='user_form'),
    path('student/<int:pk>/', views.user_detail, name='user_detail'),
    path('update/<int:pk>/', views.update, name='update'),
]