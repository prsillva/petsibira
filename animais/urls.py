from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('animais/', views.animais.as_view(), name='animais'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path('confirma-adocao/', views.confirmAdote, name='confirma-adocao'),
    path('adotar/', views.adotar_animal, name='adotar_animal'),
    path('editar/<int:id>/', views.animal_update, name='animal_update'),
    path('detalhes/<int:id>/', views.animais_detalhes, name='detalhes'),
    path('deletar/<int:id>/', views.delete_animal, name='delete')
]