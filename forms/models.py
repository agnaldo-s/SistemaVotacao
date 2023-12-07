from django.db import models
from django.contrib.auth.models import User

class Enquete(models.Model):
    pergunta = models.CharField(max_length=255)
    opcao1 = models.CharField(max_length=255)
    opcao2 = models.CharField(max_length=255)
    opcao3 = models.CharField(max_length=255)
    opcao4 = models.CharField(max_length=255)
    opcao5 = models.CharField(max_length=255)
    opcao6 = models.CharField(max_length=255)

    opcao1_resultado = models.IntegerField(default=0)
    opcao2_resultado = models.IntegerField(default=0)
    opcao3_resultado = models.IntegerField(default=0)
    opcao4_resultado = models.IntegerField(default=0)
    opcao5_resultado = models.IntegerField(default=0)
    opcao6_resultado = models.IntegerField(default=0)

    criador = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=True)
    
class Voto(models.Model):
    enquete = models.ForeignKey(Enquete, blank=False, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=10)
    votante = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)

#enquete.objects.filter(enquete_id=id, opcao1=True).count() votos opção específica
#enquete.objects.filter(enquete_id=id).count() total votos
    