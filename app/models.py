from django.db import models
from django.urls import reverse

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(choices=[('tecnologia','Tecnologia'),('vestuario','Vestuário')])
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - R${self.preco}'
    
    def get_absolute_url(self):
        return reverse('app:index', args=[self.pk])