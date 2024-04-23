from django.urls import path
from .views import dashboard


urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('create_blog/', create_blog, name='creat_blog')


]