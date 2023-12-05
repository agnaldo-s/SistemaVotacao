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
    criador = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    
class Voto(models.Model):
    enquete = models.ForeignKey(Enquete, blank=False, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=10)
    votante = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)

#enquete.objects.filter(enquete_id=id, opcao1=True).count()
    