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
from mails.models import Mail
from .serializers import MailSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': 'http://127.0.0.1:3001/mail/index.html?page='+str(self.page.number+1),
                'previous': 'http://127.0.0.1:3001/mail/index.html?page='+str(self.page.number-1)
            },
            'current': self.page.number,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })

class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None

class MailListView(ListAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']

    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class MailDetailView(RetrieveAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['order']
    ordering = ['order']

    pagination_class = NotPaginatedSetPagination
    permission_classes = (permissions.IsAuthenticated, )


class MailCreateView(CreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MailUpdateView(UpdateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MailDeleteView(DestroyAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = (permissions.IsAuthenticated, )
