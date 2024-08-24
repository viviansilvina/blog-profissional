from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Habilidades_tecnicas)
class HabilidadesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')

@admin.register(Atividades_extra)
class AtividadesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')

@admin.register(Pessoal)
class PessoalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'descricao')
    search_fields = ('titulo', 'subtitulo', 'descricao')
