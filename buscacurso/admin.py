from django.contrib import admin
from .models import Curso, Curso_Faculdade,Faculdade,Curso_teste

admin.site.register(Curso)
admin.site.register(Faculdade)
admin.site.register(Curso_Faculdade)
admin.site.register(Curso_teste)

# Register your models here.
