from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import Produto

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model
User = get_user_model()
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class LoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(label='email',max_length=200,min_length=10)
    password = serializers.CharField(label='senha',max_length=20,min_length=7,write_only=True)
    tokens = serializers.SerializerMethodField()
    proprietario = serializers.BooleanField()
    
    def get_tokens(self,obj):
        user = User.objects.get(email=obj['email'])
        
        return{
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    class Meta:
        model = User
        fields = ['id','email','password','tokens','proprietario']
        extra_kwargs = {
            'username': {'required': False, 'allow_blank': True, 'min_length': 8},
            'passoword': {'required': True, 'write_only':True, 'allow_blank': False, 'min_length': 4},
        }
        unique_together = [('email')]
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password','')
        user = auth.authenticate(email=email,password=password)
        
        if not user:
            raise AuthenticationFailed('dados errados, tente novamente')
        return{
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
            
        }