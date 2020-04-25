# from rest_framework import viewsets

# class BTypeViewSet(viewsets.ModelViewSet):
#     serializer_class = BTypeSerializer
#     queryset = BType.objects.all()

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from btypes.models import BType
from .serializers import BTypeSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': 'http://127.0.0.1:3001/btype/index.html?page='+str(self.page.number+1),
                'previous': 'http://127.0.0.1:3001/btype/index.html?page='+str(self.page.number-1)
            },
            'current': self.page.number,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })

class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None


class BTypeListView(ListAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class BTypeDetailView(RetrieveAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']
    
    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class BTypeCreateView(CreateAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BTypeUpdateView(UpdateAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BTypeDeleteView(DestroyAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
    permission_classes = (permissions.IsAuthenticated, )
