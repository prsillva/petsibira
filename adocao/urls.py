from django.urls import path
from . import views

app_name = 'adocao'

urlpatterns = [
    path('adotar/', views.register_pet, name='adotar_animal')
    
]