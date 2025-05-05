from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Processamento
from .serializers import ProcessamentoSerializer
from .task import processar_numeros

class ProcessamentoViewSet(viewsets.ModelViewSet):
    queryset = Processamento.objects.all()
    serializer_class = ProcessamentoSerializer
    def list(self, request):
        processamento = Processamento.objects.all()
        serializer = ProcessamentoSerializer(processamento, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProcessamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        processamento = serializer.save()
        processar_numeros.delay(processamento.id)

        return Response({"id": processamento.id, "status": processamento.status}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            processamento = Processamento.objects.get(id=pk)
            serializer = ProcessamentoSerializer(processamento, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            processamento = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Processamento.DoesNotExist:
            return Response({"error": "Registro não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
    def list_by_id(self, request, num=None):
        processamento = Processamento.objects.filter(num1=num)
        serializer = ProcessamentoSerializer(processamento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)