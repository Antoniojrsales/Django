from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/page/home.html', context={
        'name': 'Junior'
    })

def contato(request):
    return HttpResponse('contato1')

def sobre(request):
    return HttpResponse('sobre1')
