# from rest_framework import viewsets

# class PriorityViewSet(viewsets.ModelViewSet):
#     serializer_class = PrioritySerializer
#     queryset = Priority.objects.all()

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from priorities.models import Priority
from .serializers import PrioritySerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': 'http://127.0.0.1:3001/priority/index.html?page='+str(self.page.number+1),
                'previous': 'http://127.0.0.1:3001/priority/index.html?page='+str(self.page.number-1)
            },
            'current': self.page.number,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })

class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None

class PriorityListView(ListAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    pagination_class = NotPaginatedSetPagination     
    permission_classes = (permissions.IsAuthenticated, )


class PriorityDetailView(RetrieveAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class PriorityCreateView(CreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (permissions.IsAuthenticated, )


class PriorityUpdateView(UpdateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (permissions.IsAuthenticated, )


class PriorityDeleteView(DestroyAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (permissions.IsAuthenticated, )
