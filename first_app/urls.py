from django.urls import path
from . import views

urlpatterns = [
    
    path('index/', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('customer/', views.customer, name = 'customer'),
    path('', views.blog_page_home, name = 'blog_page_home'),

]
