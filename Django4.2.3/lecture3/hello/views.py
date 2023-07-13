from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

# def index(request):
#     return HttpResponse("Hello Rommer!")

def corazon(request):
    return HttpResponse("Hello Corazon!")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")

def greetings(request, name):
    return render(request, "hello/greetings.html", {"name": name.capitalize()})



