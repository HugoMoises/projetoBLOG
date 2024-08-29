from django.shortcuts import render
from .models import Curso, Interesse
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'blog/cursos.html', {'cursos': cursos})

def interesses(request):
    interesses = Interesse.objects.all()
    return render(request, 'blog/interesses.html', {'interesses': interesses})
