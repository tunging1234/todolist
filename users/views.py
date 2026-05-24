from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request): #首頁
    return HttpResponse("<h1>Hello!</h1>")

def profile(request):
    context={
        "name":"tang",
        "age":39,
        "heigth":159,
        "weight":79
    }
    return JsonResponse(context)