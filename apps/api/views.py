from django.shortcuts import render, redirect
from .forms import ClienteForm, HotelForm, QuartoForm, RecomendacaoForm, PessoaForm
from apps.core.models import Pessoa, Cliente, Hotel, Quarto, RecomendacaoHotel
from django.forms.models import model_to_dict
# Create your views here.


def cliente_create(request):
    context = dict()
    context['tipo'] = 'clientes'
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_edit', cliente.id)
    else:
        form = ClienteForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def cliente_view(request):
    context = dict()
    context['clientes'] = Cliente.objects.all()
    context['tipo'] = 'clientes'
    return render(request, 'view.html', context=context)

def cliente_edit(request, cliente_id):
    context = dict()
    cliente = Cliente.objects.get(id=cliente_id)
    context['cliente'] = cliente
    context['tipo'] = 'clientes'
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_view')
    else:
        form = ClienteForm(initial=model_to_dict(cliente))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def cliente_delete(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('cliente_view')
#------------------Hoteis
def hotel_create(request):
    context = dict()
    context['tipo'] = 'hoteis'
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save()
            return redirect('hotel_edit', hotel.id)
    else:
        form = HotelForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def hotel_view(request):
    context = dict()
    context['hoteis'] = Hotel.objects.all()
    context['tipo'] = 'hoteis'
    return render(request, 'view.html', context=context)

def hotel_edit(request, hotel_id):
    context = dict()
    hotel = Hotel.objects.get(id=hotel_id)
    context['hotel'] = hotel
    context['tipo'] = 'hoteis'
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_view')
    else:
        form = HotelForm(initial=model_to_dict(hotel))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def hotel_delete(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    hotel.delete()
    return redirect('hotel_view')
#------------------Quartos
def quarto_create(request):
    context = dict()
    context['tipo'] = 'quartos'
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            quarto = form.save()
            return redirect('quarto_edit', quarto.id)
    else:
        form = QuartoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def quarto_view(request):
    context = dict()
    context['quartos'] = Quarto.objects.all()
    context['tipo'] = 'quartos'
    return render(request, 'view.html', context=context)

def quarto_edit(request, quarto_id):
    context = dict()
    quarto = Quarto.objects.get(id=quarto_id)
    context['quarto'] = quarto
    context['tipo'] = 'quartos'
    if request.method == 'POST':
        form = QuartoForm(request.POST, instance=quarto)
        if form.is_valid():
            form.save()
            return redirect('quarto_view')
    else:
        form = QuartoForm(initial=model_to_dict(quarto))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def quarto_delete(request, quarto_id):
    quarto = Quarto.objects.get(id=quarto_id)
    quarto.delete()
    return redirect('quarto_view')
#---------------Recomendacoes
def recomendacao_create(request):
    context = dict()
    context['tipo'] = 'recomendacoes'
    if request.method == 'POST':
        form = RecomendacaoForm(request.POST)
        if form.is_valid():
            recomendacao = form.save()
            return redirect('recomendacao_edit', recomendacao.id)
    else:
        form = RecomendacaoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def recomendacao_view(request):
    context = dict()
    context['recomendacoes'] = RecomendacaoHotel.objects.all()
    context['tipo'] = 'recomendacoes'
    return render(request, 'view.html', context=context)

def recomendacao_edit(request, recomendacao_id):
    context = dict()
    recomendacao = RecomendacaoHotel.objects.get(id=recomendacao_id)
    context['recomendacao'] = recomendacao
    context['tipo'] = 'recomendacoes'
    if request.method == 'POST':
        form = RecomendacaoForm(request.POST, instance=recomendacao)
        if form.is_valid():
            form.save()
            return redirect('recomendacao_view')
    else:
        form = RecomendacaoForm(initial=model_to_dict(recomendacao))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def recomendacao_delete(request, recomendacao_id):
    recomendacao = RecomendacaoHotel.objects.get(id=recomendacao_id)
    recomendacao.delete()
    return redirect('recomendacao_view')
#--------------------Pessoa
def pessoa_create(request):
    context = dict()
    context['tipo'] = 'pessoas'
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            return redirect('pessoa_edit', pessoa.id)
    else:
        form = PessoaForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def pessoa_view(request):
    context = dict()
    context['pessoas'] = Pessoa.objects.all()
    context['tipo'] = 'pessoas'
    return render(request, 'view.html', context=context)

def pessoa_edit(request, pessoa_id):
    context = dict()
    pessoa = Pessoa.objects.get(id=pessoa_id)
    context['pessoa'] = pessoa
    context['tipo'] = 'pessoas'
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa_view')
    else:
        form = PessoaForm(initial=model_to_dict(pessoa))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def pessoa_delete(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa.delete()
    return redirect('pessoa_view')
