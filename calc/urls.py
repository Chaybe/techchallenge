from django.contrib import admin
from django.urls import path

from .views import ProcessamentoViewSet

urlpatterns = [
    path('processamento', ProcessamentoViewSet.as_view({
        'get': 'list', 
        'post': 'create'
    }), name='processamento-list'),
    
    path('processamento/<str:pk>', ProcessamentoViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'destroy'
    }), name='processamento-detail'),

    path('processamento/<int:num>', ProcessamentoViewSet.as_view({
        'get': 'list_by_id'
    }))
]
