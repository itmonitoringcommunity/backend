# from rest_framework import viewsets

# class StateViewSet(viewsets.ModelViewSet):
#     serializer_class = StateSerializer
#     queryset = State.objects.all()

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from states.models import State
from .serializers import StateSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': 'http://127.0.0.1:3001/state/index.html?page='+str(self.page.number+1),
                'previous': 'http://127.0.0.1:3001/state/index.html?page='+str(self.page.number-1)
            },
            'current': self.page.number,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })

class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None


class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class StateDetailView(RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class StateCreateView(CreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class StateUpdateView(UpdateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class StateDeleteView(DestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAuthenticated, )
