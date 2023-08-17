from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Index page</h1> <a href='/first_app/contact/'>Contact</a> | <a href='/first_app/about/'>About</a> | <a href='/first_app/home/'>Home</a>")
 
def home(request):
    return HttpResponse("<h1>Welcome to Home page</h1> <a href='/first_app/contact/'>Contact</a> | <a href='/first_app/about/'>About</a> | <a href='/first_app/index/'>Index</a>")

def contact(request):
    return HttpResponse("<h1>This is our Contact page</h1> <a href='/first_app/home/'>Home</a> | <a href='/first_app/about/'>About</a> | <a href='/first_app/index/'>Index</a>")

def about(request):
    return HttpResponse("<h1>This is About page</h1> <a href='/first_app/contact/'>Contact</a> | <a href='/first_app/home/'>Home</a> | <a href='/first_app/index/'>Index</a>")

def customer(request):
    return render(request, 'first_app/customer.html')