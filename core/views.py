from django.shortcuts import render, redirect
from .models import Contato
from django.contrib import messages


def login(request):
    return redirect('admin/')


def home(request):
    return render(request, 'core/index.html')


def contato(request):
    return render(request, 'core/contato.html')


def mensagem(request):
    return render(request, 'core/mensagem.html')


def pedido_novo(request):
    if request.method == 'POST':

            pedido = {}
            pedido['nome'] = request.POST.get('nome')
            pedido['telefone'] = request.POST.get('telefone')
            pedido['email'] = request.POST.get('email')
            pedido['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**pedido)
    return redirect('core_contato')