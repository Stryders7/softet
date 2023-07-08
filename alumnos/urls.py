from django.urls import path
from  . import views

urlpatterns =[
    path('', views.index,name='index'),
    path('formulario', views.formulario,name='formulario'),
    path('productos', views.productos,name='productos'),
    path('cosas', views.cosas,name='cosas'),
]