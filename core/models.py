from django.db import models
from django.utils.text import slugify
from django.db.models import signals


class Base(models.Model):
    criado = models.DateField('data de criação', auto_now_add=True)
    modificado = models.DateField('data de atualização',auto_now=True)
    ativo = models.BooleanField('Ativo?',default=True)
    class Meta:
        abstract=True
class Produto(Base):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço',max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    def _str_(self):
        return self.nome
def produto_pre_save(signal,instance,sender,**kwargs):
    instance.slug =slugify(instance.nome)
signals.pre_save.connect(produto_pre_save, sender=Produto)
