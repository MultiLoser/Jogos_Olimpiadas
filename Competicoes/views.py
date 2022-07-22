from django.shortcuts import render
from .forms import ParticipanteForm
from .models import Competicao
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

def ranking(request):
    ranking_01 = Competicao.objects.get(pk = 1).participante_set.all().order_by('pontuacao_metros_rasos')
    ranking_02 = Competicao.objects.get(pk = 2).participante_set.all().order_by('-pontuacao_dardos')
    return render(request, 'competicoes/ranking.html', {'ranking01' : ranking_01, 'ranking02' : ranking_02})
