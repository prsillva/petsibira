from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('criar/', views.post_create, name='post_create'),
    path('editar/<int:id>/', views.post_update, name='post_update'),
    path('deletar/<int:id>/', views.post_delete, name='post_delete'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('duvidas/', views.duvidas, name='duvidas'),
    path('voluntarios/', views.voluntarios, name='voluntarios'),
    path('duvidas-voluntarios/', views.duvidas_voluntario, name='duvidas_voluntario'),
    path('form-voluntarios/', views.form_voluntario, name='form_voluntario'),
    path('pagina-responsabilidades/', views.page_responsabilidades, name='page_responsabilidades'),
    
]