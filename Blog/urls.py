from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashborad, name='dashboard'),
    path('create/', views.create_blog_view, name='create_blog'),
    path('blog_list/', views.list_blogs_view, name='blog_list'),
    path('update/<int:blog_id>/', views.update_blog_view, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog_view, name='delete_blog'),
]