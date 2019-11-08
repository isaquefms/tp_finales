from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField(verbose_name='Nome', max_length=100)
	cpf = models.CharField(verbose_name='CPF', max_length=14)
	email = models.EmailField(verbose_name='Email')
	# user = models.OneToOneField(verbose_name='Usuario', to=User, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class Cliente(models.Model):
	telefone = models.CharField(verbose_name='Telefone', max_length=14)
	pessoa = models.OneToOneField(verbose_name='Pessoa', to=Pessoa, on_delete=models.CASCADE)

	def __str__(self):
		return self.pessoa.nome


class Hotel(models.Model):
	nome = models.CharField(verbose_name='Nome', max_length=100)
	descricao_hotel = models.CharField(verbose_name='Descrição Hotel', max_length=500, null=True, blank=True)
	# foto = models.ImageField(upload_to='/imgs/hoteis/', null=True, blank=True)

	def __str__(self):
		return self.nome


class Quarto(models.Model):
	hotel = models.ForeignKey(verbose_name='Hotel', to=Hotel, on_delete=models.CASCADE)
	num_quarto = models.IntegerField(verbose_name='Número de Quartos')
	num_camas_solteiro = models.IntegerField(verbose_name='Camas de Solteiro')
	num_camas_casal = models.IntegerField(verbose_name='Camas de Casal')

	def __str__(self):
		return 'Quarto no hotel ' + self.hotel.nome


class RecomendacaoHotel(models.Model):
	hotel = models.ForeignKey(verbose_name='Hotel', to=Hotel, on_delete=models.CASCADE)
	cliente = models.ForeignKey(verbose_name='Cliente', to=Cliente, on_delete=models.CASCADE)
	descricao = models.TextField(verbose_name='Descrição', null=True, blank=True)
