from django.contrib import admin
from django.urls import path

from .views import ProcessamentoViewSet

urlpatterns = [
    path('processamento', ProcessamentoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='processamento-list-create'),
    
    path('processamento/<str:pk>', ProcessamentoViewSet.as_view({
        'put': 'update',
    }), name='processamento-detail'),
    
    path('status/<int:pk>', ProcessamentoViewSet.as_view({
        'get': 'list_by_id',
    }), name='processamento-status'),
]
