from django.shortcuts import render

from django.http import HttpResponse
from .forms import EstadioForm
from .models import Estadio
def inicio(request):
    
    return render(request, 'AppClub/inicio.html')


def plantel(request):
    
    return render(request, 'AppClub/plantel.html')


def disciplinas(request):
    
    return render(request, 'AppClub/disciplinas.html')

def estadio(request):

    if request.method == "POST":
        formularioEstadio = EstadioForm(request.POST)
        if formularioEstadio.is_valid():
            informacion = formularioEstadio.cleaned_data
            estadio = Estadio()
            estadio.nombre = informacion['nombre']
            estadio.direccion = informacion['direccion']
            estadio.anioFund = informacion['anioFund']
            estadio.save()
    else:
        formularioEstadio = EstadioForm()

    return render(request, 'AppClub/estadio.html')

