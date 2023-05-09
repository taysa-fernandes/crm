from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import Produto
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model

User = get_user_model()
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True,error_messages={'required': 'Por favor, informe seu nome de usuário'})
    password = serializers.CharField(required=True, write_only=True,error_messages={'required': 'Por favor, informe sua senha'})

