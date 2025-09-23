from django.shortcuts import render, get_object_or_404
from .models import Produto

def index(request):
    return render(request, 'index.html')

def tecnologia(request):
    produtosTec = Produto.objects.filter(categoria="tecnologia")
    return render(request, 'tecnologia.html', {'produtosTec': produtosTec})

def vestuario(request):
    produtosVest = Produto.objects.filter(categoria="vestuario")
    return render(request, 'vestuario.html', {'produtosVest':produtosVest})

def detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes.html', {'produto':produto})