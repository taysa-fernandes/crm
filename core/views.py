
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ProdutoModelForm
from .models import Produto

from django.http import HttpResponse
from django.template import loader

from .forms import ProdutoForm


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def produto(request):
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            preco = form.cleaned_data['preco']
            estoque = form.cleaned_data['estoque']
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('index')
    else:
        form = ProdutoForm()
    return render(request, 'produto.html', {'form': form})

def atualizar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoModelForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {'produto': produto, 'form': form}
    return render(request, 'atualizar.html', context)

def deletar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto deletado com sucesso!')
        return redirect('index')
    return render(request, 'deletar.html', {'produto': produto})
def vender(request,pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade'))
        if quantidade > produto.estoque:
            messages.error(request, f"A quantidade solicitada ({quantidade}) é maior do que o estoque disponível ({produto.estoque}).")
        else:
            produto.estoque -= quantidade
            produto.save()
            messages.success(request, f"{quantidade} unidades do produto {produto.nome} foram vendidas com sucesso!")
            return redirect('index')
    return render(request, 'vender.html', {'produto': produto})
def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8',status=404)
def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8',status=500)