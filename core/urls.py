from django.urls import path

from .views import  index,produto,atualizar,deletar

urlpatterns=[
    path('',index, name='index'),
    path('produto',produto, name='produto'),
    path('atualizar/<int:pk>',atualizar, name='atualizar'),
    path('deletar/<int:pk>',deletar, name='deletar'),
]