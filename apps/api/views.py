from django.shortcuts import render, redirect
from api.forms import PessoaForm, HotelForm, QuartoForm, RecomendacaoForm, PessoaForm
# Create your views here.


def cliente_create(request):
    context = dict()
    context['tipo'] = 'clientes'
    context['form'] = ClienteForm()
    return render(request, 'create.html')

def cliente_view(request):
    context = dict()
    context['clientes'] = Cliente.objects.all()
    context['tipo'] = 'clientes'
    return render(request, 'view.html')

def cliente_edit(request, cliente_id):
    context = dict()
    cliente = Cliente.objects.get(id=cliente_id)
    context['cliente'] = cliente
    context['tipo'] = 'clientes'
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm(initial=model_to_dict(cliente))
        context['form'] = form
    return render(request, 'edit.html')

def cliente_delete(request, cliente_id):
    context = dict()
    Hotel.objects.delete(id=cliente_id)
    context['tipo'] = 'clientes'
    return redirect('cliente_view')
#------------------Hoteis
def hotel_create(request):
    context = dict()
    context['tipo'] = 'hoteis'
    context['form'] = HotelForm()
    return render(request, 'create.html')

def hotel_view(request):
    context = dict()
    context['clientes'] = Hotel.objects.all()
    context['tipo'] = 'hoteis'
    return render(request, 'view.html')

def hotel_edit(request, hotel_id):
    context = dict()
    hotel = Hotel.objects.get(id=hotel_id)
    context['hotel'] = hotel
    context['tipo'] = 'hoteis'
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HotelForm(initial=model_to_dict(hotel))
        context['form'] = form
    return render(request, 'edit.html')

def hotel_delete(request, hotel_id):
    context = dict()
    Hotel.objects.delete(id=hotel_id)
    context['tipo'] = 'hoteis'
    return redirect('hotel_view')
#------------------Quartos
def quarto_create(request):
    context = dict()
    context['tipo'] = 'quartos'
    context['form'] = QuartoForm()
    return render(request, 'create.html')

def quarto_view(request):
    context = dict()
    context['quartos'] = Quarto.objects.all()
    context['tipo'] = 'quartos'
    return render(request, 'view.html')

def quarto_edit(request, quarto_id):
    context = dict()
    quarto = Quarto.objects.get(id=quarto_id)
    context['quarto'] = quarto
    context['tipo'] = 'quartos'
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuartoForm(initial=model_to_dict(quarto))
        context['form'] = form
    return render(request, 'edit.html')

def quarto_delete(request, quarto_id):
    context = dict()
    Quarto.objects.delete(id=quarto_id)
    context['tipo'] = 'quartos'
    return redirect('quarto_view')
#---------------Recomendacoes
def recomendacao_create(request):
    context = dict()
    context['tipo'] = 'recomendacoes'
    context['form'] = RecomendacaoForm()
    return render(request, 'create.html')

def recomendacao_view(request):
    context = dict()
    context['clientes'] = Recomendacao.objects.all()
    context['tipo'] = 'recomendacoes'
    return render(request, 'view.html')

def recomendacao_edit(request, recomendacao_id):
    context = dict()
    recomendacao = Recomendacao.objects.get(id=recomendacao_id)
    context['recomendacao'] = recomendacao
    context['tipo'] = 'recomendacoes'
    if request.method == 'POST':
        form = RecomendacaoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecomendacaoForm(initial=model_to_dict(recomendacao))
        context['form'] = form
    return render(request, 'edit.html')

def recomendacao_delete(request, recomendacao_id):
    context = dict()
    Recomendacao.objects.delete(id=recomendacao_id)
    context['tipo'] = 'recomendacoes'
    return redirect('recomendacao_view')
#--------------------Pessoa
def pessoa_create(request):
    context = dict()
    context['tipo'] = 'pessoas'
    context['form'] = PessoaForm()
    return render(request, 'create.html')

def pessoa_view(request):
    context = dict()
    context['pessoas'] = Pessoa.objects.all()
    context['tipo'] = 'pessoas'
    return render(request, 'view.html')

def pessoa_edit(request, pessoa_id):
    context = dict()
    pessoa = Pessoa.objects.get(id=pessoa_id)
    context['pessoa'] = pessoa
    context['tipo'] = 'pessoas'
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PessoaForm(initial=model_to_dict(pessoa))
        context['form'] = form
    return render(request, 'edit.html')

def pessoa_delete(request, pessoa_id):
    context = dict()
    Hotel.objects.delete(id=pessoa_id)
    context['tipo'] = 'pessoas'
    return redirect('pessoa_view')
