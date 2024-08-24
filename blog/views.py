from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def academico(request):
    habilidades = Habilidades_tecnicas.objects.all()
    atividades = Atividades_extra.objects.all()
    contexto = {
        'lista': habilidades,
        'cursos': atividades,
    }
    return render(request, 'academico.html', contexto)

def pessoal(request):
    publicacao = Pessoal.objects.all()
    contexto = {
        'posts': publicacao,
    }

    return render(request, 'pessoal.html', contexto)
