from django.db import models

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField(verbose_name='Nome', max_lenght=100)
	cpf = models.CharField(verbose_name='CPF', max_lenght=14)
	email = models.EmailField(verbose_name='Email')

	def __str__(self):
		return self.nome


class Cliente(Pessoa):
	telefone = models.CharField(verbose_name='Telefone', max_lenght=14)


class Recomendavel(models.Model):
	