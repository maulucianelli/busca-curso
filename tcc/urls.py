from django.urls import path
from.import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/', views.helloworld),
    path('tcc/',views.tcc),
]