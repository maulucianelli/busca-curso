from django.shortcuts import render


def index (request):
    return render(request, 'index.html')

#passo 2 criar função

def course_list(request):
    return render(request, 'course_list.html')

def details(request):
    return render(request, 'details.html')

def support(request):
    return render(request, 'support.html')
