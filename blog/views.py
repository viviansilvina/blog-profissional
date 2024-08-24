from django.shortcuts import render
from .models import Interesses

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def academico(request):
    interesse = Interesses.objects.all()
    contexto = {
        'lista': interesse
    }
    return render(request, 'academico.html', contexto)

def pessoal(request):
    return render(request, 'pessoal.html')
