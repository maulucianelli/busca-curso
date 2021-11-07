from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    #path para index
    path('', views.index, name='index'),
    #criar nova janela PASSO 1
    path('course_list', views.course_list, name='course_list'),
    path('details/<int:pk>/', views.details, name='details'),
    path('support', views.support, name='support'),
]