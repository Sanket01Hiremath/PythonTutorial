from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome")


def greet(request,name):
    return HttpResponse(f"Hello,{name}")

def farewell(request,name):
    return HttpResponse(f"GoodBye,{name}")