"""recmmnd URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.api.views import pessoa_create, pessoa_view, pessoa_edit, pessoa_delete, cliente_create, cliente_view, cliente_edit, cliente_delete, hotel_view, hotel_create, hotel_edit, hotel_delete, quarto_view, quarto_create, quarto_edit, quarto_delete, recomendacao_view, recomendacao_create, recomendacao_edit, recomendacao_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    #Pessoa
    path('pessoa/create', pessoa_create, name='pessoa_create'),
    path('pessoa/view', pessoa_view, name='pessoa_view'),
    path('pessoa/edit/<int:pessoa_id>', pessoa_edit, name='pessoa_edit'),
    path('pessoa/delete/<int:pessoa_id>', pessoa_delete, name='pessoa_delete'),
    #Cliente
    path('cliente/create', cliente_create, name='cliente_create'),
    path('cliente/view', cliente_view, name='cliente_view'),
    path('cliente/edit/<int:cliente_id>', cliente_edit, name='cliente_edit'),
    path('cliente/delete/<int:cliente_id>', cliente_delete, name='cliente_delete'),
    #Hotel
    path('hotel/create', hotel_create, name='hotel_create'),
    path('hotel/view', hotel_view, name='hotel_view'),
    path('hotel/edit/<int:hotel_id>', hotel_edit, name='hotel_edit'),
    path('hotel/delete/<int:hotel_id>', hotel_delete, name='hotel_delete'),
    #Quarto
    path('quarto/create', quarto_create, name='quarto_create'),
    path('quarto/view', quarto_view, name='quarto_view'),
    path('quarto/edit/<int:quarto_id>', quarto_edit, name='quarto_edit'),
    path('quarto/delete/<int:quarto_id>', quarto_delete, name='quarto_delete'),
    #Recomendacao
    path('recomendacao/create', recomendacao_create, name='recomendacao_create'),
    path('recomendacao/view', recomendacao_view, name='recomendacao_view'),
    path('recomendacao/edit/<int:recomendacao_id>', recomendacao_edit, name='recomendacao_edit'),
    path('recomendacao/delete/<int:recomendacao_id>', recomendacao_delete, name='recomendacao_delete'),
]
