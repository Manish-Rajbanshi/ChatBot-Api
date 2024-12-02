from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request , "home/index.html")

def login(request):
    return render(request , "home/login.html")

def signup(request):
    return render(request , "home/signup.html")

def profile(request):
    return render(request , "home/profile.html")

def history(request):
    return render(request , "home/history.html")

def base(request):
    return render(request , "home/base.html")

def success_page(request):
    return HttpResponse("<h1>hi I'm success_page</h1>")