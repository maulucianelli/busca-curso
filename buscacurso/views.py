from django.shortcuts import get_object_or_404, render
#from .models import Curso, Curso_teste, Faculdade
from .models import *
import requests
from django.shortcuts import render
from tcc import settings

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
    course_name = 'administracao'
    response = requests.get("https://api.educamaisbrasil.com.br/api/Curso/ConsultarSalarioPorteCargo?cursoUrl="+ course_name)
    if response.status_code == 200:
        salarydata = response.json()
        print("deu bom", response.status_code)
    else:
        print("deu ruim" , response)
    eachInstitution= CoursesInstitution.objects.all
    #course=Courses.objects.get(code=pk)
    eachCourse= Courses.objects.get(code=pk)
    institution=Institution.objects.filter(title=pk)
    #context['admin_category'] = institution.admin_category_display()
    details ={
        'eachCourse' :  eachCourse,
        'eachInstitution': eachInstitution,
        'institution': institution,
    }
    if len(salarydata)>0:
        details['trainee']= salarydata[1]["SALARIO_TRAINEE"]
        details['pleno']= salarydata[1]["SALARIO_PLENO"]
        details['senior']= salarydata[1]["SALARIO_SENIOR"]

    return render(request, 'details.html',details)

def support(request):
    return render(request, 'support.html')


