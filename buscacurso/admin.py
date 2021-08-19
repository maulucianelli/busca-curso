from django.contrib import admin
from .models import Curso, Curso_Faculdade,Faculdade

admin.site.register(Curso)
admin.site.register(Faculdade)
admin.site.register(Curso_Faculdade)


# Register your models here.
