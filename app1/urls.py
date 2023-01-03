from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home.as_view(), name='home'),

    path('hello/', views.HelloView.as_view(), name='hello'),
]