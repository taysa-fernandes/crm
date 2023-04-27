from django.urls import path

from .views import  index,produto,atualizar,deletar,vender,ProdutoList,ProdutoDetail,register_user
from . import views


urlpatterns=[
    path('',index, name='index'),
    path('produto',produto, name='produto'),
    path('atualizar/<int:pk>',atualizar, name='atualizar'),
    path('deletar/<int:pk>',deletar, name='deletar'),
    path('vender/<int:pk>',vender,name='vender'),
    path('produtos/', ProdutoList.as_view(), name='produto_list'),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name='produto_detail'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', register_user, name='register_user'),
]
