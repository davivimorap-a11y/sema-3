
from django.shortcuts import render
from .models import Artista, Genero


def inicio(request):
    artistas = Artista.objects.prefetch_related(
        'albumes__canciones'
    ).all()

    generos = Genero.objects.all()

    return render(request, 'index.html', {
        'artistas': artistas,
        'generos': generos,
    })

