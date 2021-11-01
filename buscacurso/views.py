from django.shortcuts import get_object_or_404, render
#from .models import Curso, Curso_teste, Faculdade
from .models import *
import requests
from django.shortcuts import render
import base64
from django.core.exceptions import MultipleObjectsReturned
from django.core import serializers

def index (request):
    return render(request, 'index.html')

#passo 2 criar função
##def course_list(request):
#    faculdades= Curso_teste.objects.all
#
 #   dados = {
  #      'faculdades' :faculdades
   # }

    return render(request, 'course_list.html',dados)
def course_list(request):
    courses_inst= CoursesInstitution.objects.all
    courses=Courses.objects.all
    institution=Institution.objects.all
    maintainer=Maintainer.objects.all

    dados = {
        'courses_inst' : courses_inst,
        'courses' : courses,
        'institution' : institution,
        'maintainer' : maintainer
    }

    return render(request, 'course_list.html',dados)

def details(request,pk):
    eachInstitution= CoursesInstitution.objects.all
    #course=Courses.objects.get(code=pk)
    eachCourse= Courses.objects.get(code=pk)
    institution=Institution.objects.filter(title=pk)
    #context['admin_category'] = institution.admin_category_display()
    testJson = serializers.serialize('json', [eachCourse])
    details ={
        'eachCourse' :  eachCourse,
        'eachInstitution': eachInstitution,
        'institution': institution,
        'test': testJson
    }
    return render(request, 'details.html',details)

def support(request):
    return render(request, 'support.html')


