from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Processamento
from .serializers import ProcessamentoSerializer
from .task import processar_numeros

class ProcessamentoViewSet(viewsets.ModelViewSet):
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

    def retrieve(self, request, pk=None):
        processamento = Processamento.objects.get(id=pk)
        serializer = ProcessamentoSerializer(processamento)
        return Response(serializer.data)
