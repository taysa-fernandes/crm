from django.urls import path

from .views import  index,produto,atualizar,deletar

urlpatterns=[
    path('',index, name='index'),
    path('produto',produto, name='produto'),
    path('atualizar',atualizar, name='atualizar'),
    path('deletar',deletar, name='deletar'),
]