
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
    if str(request.user) != 'AnonymousUser':
        produto = get_object_or_404(Produto, pk=pk)
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES, instance=produto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto atualizado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao atualizar produto!')
        else:
            form = ProdutoModelForm(instance=produto)
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

def deletar(request, pk):
    if str(request.user) != 'AnonymousUser':
        produto = get_object_or_404(Produto, pk=pk)
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('index')
    else:
        return redirect('index')
def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8',status=404)
def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),content_type='text/html; charset=utf8',status=500)