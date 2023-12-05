from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Enquete(models.Model):
    pergunta = models.CharField(max_length=255)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    encerrada = models.BooleanField(default=False)

    def __str__(self):
        return self.pergunta
    
    def clean(self):
        opcoes_count = self.opcao_set.count()

        if opcoes_count < 2:
            raise ValidationError("A enquete deve ter pelo menos 2 opções.")

        if opcoes_count > 4:
            raise ValidationError("A enquete não pode ter mais do que 4 opções.")

class Opcao(models.Model):
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE)
    texto_opcao = models.CharField(max_length=255)
    votos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.texto_opcao

class Voto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)

class ResultadoEnquete(models.Model):
    enquete = models.OneToOneField(Enquete, on_delete=models.CASCADE)
    opcoes_votos = models.JSONField(default=dict)
