from django.contrib import admin
from apps.core.models import Pessoa, Cliente, Hotel, Quarto, RecomendacaoHotel
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Cliente)
admin.site.register(Hotel)
admin.site.register(Quarto)
admin.site.register(RecomendacaoHotel)
