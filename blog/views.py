from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def academico(request):
    return render(request, 'academico.html')

def pessoal(request):
    return render(request, 'pessoal.html')
