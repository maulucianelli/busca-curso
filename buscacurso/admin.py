from django.contrib import admin
from .models import Curso, Curso_Faculdade,Faculdade, Person

admin.site.register(Curso)
admin.site.register(Faculdade)
admin.site.register(Curso_Faculdade)
admin.site.register(Person)

# Register your models here.
