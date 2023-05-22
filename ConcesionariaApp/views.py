from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ConcesionariaApp/home.html")

def login(request):
    return render(request, "ConcesionariaApp/login.html")