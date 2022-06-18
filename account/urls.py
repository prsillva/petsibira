from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('adm/usuarios/registrar/', views.register.as_view(), name='registre')
]