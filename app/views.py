from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def inicio(request):
#     return HttpResponse("<h1> Hola </h1>")

def index(request):
    return render(request,'pages/index.html',)
