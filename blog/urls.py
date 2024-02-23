from django.urls import path
from .views import blog_list, blog_create, blog_detail

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('blog/<int:pk>', blog_detail, name='blog_detail'),


]
