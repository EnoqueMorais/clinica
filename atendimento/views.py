from django.shortcuts import render
from . models import Cliente


# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/list.html',{'clientes':clientes})    