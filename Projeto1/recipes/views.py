from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home1')

def contato(request):
    return HttpResponse('contato1')

def sobre(request):
    return HttpResponse('sobre1')
