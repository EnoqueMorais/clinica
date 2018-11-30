from django.shortcuts import render
from . models import Cliente
from . models import Medico

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/list.html',{'clientes':clientes}) 
    
def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'cliente/show.html',{'cliente':cliente})  

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/list.html',{'medicos':medicos})  

