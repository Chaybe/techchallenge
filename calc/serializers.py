from rest_framework import serializers
from .models import Processamento

class ProcessamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processamento
        fields = '__all__'

class ProcessamentoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processamento
        fields = ['num1', 'num2', 'num3']

class ProcessamentoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processamento
        fields = ['id', 'status', 'media', 'mediana']