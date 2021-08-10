from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World ! 1234')

def tcc(request):
    return render(request, 'tcc/index.html')
