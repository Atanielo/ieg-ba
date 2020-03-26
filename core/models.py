from django.db import models

# Create your models here.


class Contato(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False, verbose_name='nome')
    email = models.EmailField(max_length=40, null=False, blank=False, verbose_name='email')
    telefone = models.CharField(max_length=15, null=False, blank=False, verbose_name='telefone')
    mensagem = models.TextField()

    def __str__(self):
        return self.nome