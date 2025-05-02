from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Processamento
from .serializers import ProcessamentoSerializer

from .task import hello

class ProcessamentoViewSet(viewsets.ModelViewSet):
    def list(self, request):
        processamento = Processamento.objects.all()
        serializer = ProcessamentoSerializer(processamento, many=True)
        hello.delay("Chaybe Lucas")
        return Response(serializer.data)

    def create(self, request):
        serializer = ProcessamentoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        processamento = Processamento.objects.get(pk=pk)
        serializer = ProcessamentoSerializer(processamento)
        return Response(serializer.data)

    def update(self, request, pk=None):
        processamento = Processamento.objects.get(pk=pk)
        serializer = ProcessamentoSerializer(instance=processamento, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        pass

    def delete(self, request, pk=None):
        pass
