from django.urls import path
from . import views

app_name = 'doacao'

urlpatterns = [
    path('', views.doar_animal, name='doacao'),
    path('doar/', views.voluntario, name='doar'),
]