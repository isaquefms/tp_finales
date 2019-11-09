from django import forms
from django.forms import ModelForm
from apps.core.models import Pessoa, Cliente, Hotel, Quarto, RecomendacaoHotel

#-----------Pessoa
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

#-----------Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

#-----------Hotel
class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

#-----------Quarto
class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = '__all__'

#-----------Recomendacao
class RecomendacaoForm(forms.ModelForm):
    class Meta:
        model = RecomendacaoHotel
        fields = '__all__'
