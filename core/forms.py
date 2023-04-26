from django import forms

from .models import Produto

class ProdutoForm(forms.Form):
    nome = forms.CharField(label='nome',max_length=100)
    preco = forms.DecimalField(label='Preco',max_digits=8, decimal_places=2)
    estoque = forms.IntegerField(label='Estoque')
    def save(self, commit=True):
        produto = Produto(nome=self.cleaned_data['nome'], preco=self.cleaned_data['preco'], estoque=self.cleaned_data['estoque'])
        if commit:
            produto.save()
        return produto
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']