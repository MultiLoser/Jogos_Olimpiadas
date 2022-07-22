from django.db import models

# Create your models here.

class Competicao(models.Model):
    nome = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    altura = models.DecimalField(max_digits=10 ,decimal_places=2)
    peso = models.IntegerField()
    pontuacao_dardos = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    pontuacao_metros_rasos = models.DecimalField(max_digits=10, decimal_places=3, default=None)
    modelo_competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE, blank=True, null=True)
