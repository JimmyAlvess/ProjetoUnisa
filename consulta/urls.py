from django.urls import path

from . import views

app_name = 'clinica'
urlpatterns = [
    path('', views.ListViewBase.as_view(), name='home'),
    path('home/search/', views.ListViewSearch.as_view(), name='search'),
    path('home/<int:pk>/', views.MedicoView.as_view(), name='medico'),
    path('home/especialidade/<int:especialidade_id>/',
         views.ListViewEspecialidade.as_view(), name='especialidade'),
]
