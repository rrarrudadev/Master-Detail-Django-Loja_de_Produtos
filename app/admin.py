from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco')
    search_fields = ('nome', 'categoria')