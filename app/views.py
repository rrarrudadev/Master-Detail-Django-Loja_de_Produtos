from django.shortcuts import render, get_object_or_404
from .models import Produto

def tecnologia(request):
    produtosTec = Produto.objects.all()
    return render(request, 'tecnologia.html', {'produtosTec': produtosTec})

def vestuario(request):
    produtosVest = Produto.objects.all()
    return render(request, 'vestuario.html', {'produtosVest':produtosVest})

def detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes.html', {'produto':produto})