from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Processamento
from .serializers import ProcessamentoSerializer, ProcessamentoCreateSerializer, ProcessamentoStatusSerializer
from .task import processar_numeros

class ProcessamentoViewSet(viewsets.ModelViewSet):

    def list(self, request):
        try:
            processamento = Processamento.objects.all()
            serializer = ProcessamentoSerializer(processamento, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = ProcessamentoCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            processamento = serializer.save()
            
            processar_numeros.delay(processamento.id)

            return Response({"id": processamento.id, "status": processamento.status}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            processamento = Processamento.objects.get(id=pk)
            serializer = ProcessamentoSerializer(processamento, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            processamento = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Processamento.DoesNotExist:
            return Response({"error": "Registro não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
    def list_by_id(self, request, pk=None):
        try:
            processamento = Processamento.objects.get(id=pk)
            serializer = ProcessamentoStatusSerializer(processamento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Processamento.DoesNotExist:
            return Response({"error": "Registro não encontrado."}, status=status.HTTP_404_NOT_FOUND)    