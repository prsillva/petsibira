from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('animais/', views.listar_animais, name='listar_animais'),
    path('doar/', views.doar_animal, name='doar'),
    path('sobre/', views.sobre, name='sobre'),
    path('duvidas/', views.duvidas, name='duvidas'),
    path('voluntarios/', views.voluntarios, name='voluntarios'),
]