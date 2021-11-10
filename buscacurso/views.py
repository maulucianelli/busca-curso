from django.db.models.expressions import OrderBy
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
    #MyModel.objects.filter(blah=blah).first()
   # courses_inst= CoursesInstitution.objects.all
    courses_dict = {}
    courses=Courses.objects.all()
    for item in courses:
        courses_dict[item.name] = item
    #courses_list = [course.name for course in courses]
    #institution=Institution.objects.all
  #  maintainer=Maintainer.objects.all

    dados = {
        #'courses' : set(courses_list),
        'courses' : courses_dict
        }

    return render(request, 'course_list.html',dados)

def details(request,pk):
    eachInstitution= CoursesInstitution.objects.all
    eachCourse= Courses.objects.filter(id=pk).first()
    institution=Institution.objects.filter(title=pk)
    testJson = serializers.serialize('json', [eachCourse])
    details ={
        'eachCourse' :  eachCourse,
        'eachInstitution': eachInstitution,
        'institution': institution,
        'test': testJson,

    }
    return render(request, 'details.html',details)

def support(request):
    return render(request, 'support.html')


