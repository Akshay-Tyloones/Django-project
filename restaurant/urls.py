from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),

]