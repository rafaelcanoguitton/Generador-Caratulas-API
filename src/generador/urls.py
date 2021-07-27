from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('retornar_caratula/<str:id>', views.retornar_caratula, name='retornar_caratula'),
]