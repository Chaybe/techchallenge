from rest_framework import serializers
from .models import Processamento

class ProcessamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processamento
        fields = '__all__'
        #read_only_fields = ['media', 'mediana', 'status']
