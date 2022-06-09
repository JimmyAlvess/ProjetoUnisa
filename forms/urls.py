from django.urls import path

from . import views

app_name = 'formu'
urlpatterns = [

    path('formulario/<int:id>/', views.formulario, name='formulario'),
    path('formulario/create/', views.verifica_formulario, name='create')
]
