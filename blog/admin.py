from django.contrib import admin
from .models import Interesses
# Register your models here.
@admin.register(Interesses)
class InteressesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')
