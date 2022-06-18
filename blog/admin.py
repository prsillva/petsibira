from django.contrib import admin
from django.utils.html import format_html
from blog.models import Post, RacaAnimal, Animais, TipoAnimal
from doacao.models import Doador
from adocao.models import Adotante
from home.models import Sobre, Duvidas, Voluntarios

admin.site.register(Sobre)
admin.site.register(Doador)
admin.site.register(Adotante)
admin.site.register(Duvidas)
admin.site.register(Voluntarios)

class Adotante(admin.ModelAdmin):
    list_display = ("id","NomeAdotante","TelefoneAdotante","EmailAdotante","CepAdotante","RuaAdotante", "NumCasaAdotante","BairroAdotante","CidadeAdotante","AnimalAdotante","ObsAdotante")

class Doador(admin.ModelAdmin):
    list_display = ("id","NomeDoador","TelefoneDoador","EmailDoador","TipoDoacao","QtdDoacao", "CepDoador","RuaDoador","NumeroCasaDoador","BairroDoador","Observacao","DeAcordoDoador")

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'created_at', 'updated_at', 'status')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

class RacaAdmin(admin.ModelAdmin):
    list_display = ("id","TipoAnimal","RacaAnimal")


class AnimalAdmin(admin.ModelAdmin):
    list_display = ("id","NomeAnimal","RacaAnimal","PesoAnimal","CorAnimal","Vacinado", "Adotado","Observacao")


class TipoAnimalAdmin(admin.ModelAdmin):
    list_display = ("id","TipoAnimal")

admin.site.site_header = 'Administração - Pets Ibirá'
admin.site.index_title = 'Administração do Site'
admin.site.site_title = 'HTML title from adminsitration'
admin.site.login_title = 'Login'
admin.site.register(Animais, AnimalAdmin)
admin.site.register(RacaAnimal, RacaAdmin)
admin.site.register(TipoAnimal, TipoAnimalAdmin)

class SobreAdmin(admin.ModelAdmin):
    
    def foto_preview(self, obj):
            return format_html(
        f"<img src='{obj.imagem_sobre.url}' width='{obj.imagem_sobre.width}' height='{obj.imagem_sobre.height}' style='border-radius: 50% 50%;'/>")
    readonly_fields = ['foto_preview']
    list_display = ("id","titulo", "imagem_sobre", "texto_sobre", "status")


class DuvidasAdmin(admin.ModelAdmin):
    list_display = ("id","pergunta", "texto_pergunta")