from django.db import models
from django.utils.text import slugify
from django.db.models import signals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import UserManager 
from rest_framework_simplejwt.tokens import RefreshToken




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
    saldo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    def _str_(self):
        return self.nome
def produto_pre_save(signal,instance,sender,**kwargs):
    instance.slug =slugify(instance.nome)
signals.pre_save.connect(produto_pre_save, sender=Produto)
class User(AbstractBaseUser,PermissionRequiredMixin):
    username = models.CharField('nome de usuário',max_length=100, db_index=True)
    email = models.EmailField('Email',max_length=90,unique=True,db_index=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    proprietario = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    def get_token_access(self):
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)
    class Meta:
        verbose_name = 'Usuário'