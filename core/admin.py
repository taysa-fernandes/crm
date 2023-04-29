from django.contrib import admin

from .models import Produto,User,UserManager

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display= ('nome','preco','estoque','criado','modificado','ativo')
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display  = ('username','proprietario','email')