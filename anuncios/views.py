from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Categoria, Anuncio

def home(request):
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.all()
    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios})

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()

    categoria = get_object_or_404(Categoria, id=categoria_id)

    anuncios = Anuncio.objects.filter(categoria=categoria)

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios,
                                         'categoria': categoria})