from django.db import models
from django.utils import timezone

class Perguntas(models.Model):
	nome = models.CharField(max_length=200, default='Anônimo')
	texto = models.TextField()
	data = models.DateField(auto_now=True)

	class Meta:
		verbose_name = 'Pergunta'
		verbose_name_plural = 'Perguntas'

	def __str__(self):
		return self.nome