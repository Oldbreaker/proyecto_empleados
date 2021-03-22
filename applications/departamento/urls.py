from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'
urlpatterns = [
    path('new-departamento/', views.NewDepartamentroView.as_view(),
         name='nuevo_departamento'),
    path('listar-departamentos/', views.DepartamentoListView.as_view(),
         name='list-departamentos'),
]
