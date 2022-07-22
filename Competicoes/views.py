from django.shortcuts import render
from .forms import ParticipanteForm
# Create your views here.


def index(request):
    return render(request, 'competicoes/index.html', None)


def formulario(request):
    if request.method == 'GET':
        form = ParticipanteForm()
        contexto = {
            'form' : form
        }
        return render(request, 'competicoes/formulario.html', contexto)
    else:
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save()
            form = ParticipanteForm()

        contexto = {
            'form': form
        }
        return render(request, 'competicoes/formulario.html', contexto)
