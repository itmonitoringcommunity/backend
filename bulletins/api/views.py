# from rest_framework import viewsets

# class BulletinViewSet(viewsets.ModelViewSet):
#     serializer_class = BulletinSerializer
#     queryset = Bulletin.objects.all()

import sys, os

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath('pylibs')), 'pylibs'))

from pylibs import CustomBulletin
cblt = CustomBulletin()

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bulletins.models import Bulletin
from .serializers import BulletinSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': 'http://127.0.0.1:3001/bulletin/index.html?page='+str(self.page.number+1),
                'previous': 'http://127.0.0.1:3001/bulletin/index.html?page='+str(self.page.number-1)
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })

class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None

class BulletinListView(ListAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^code', '^title']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['begin_time']
    ordering = ['-begin_time']

    pagination_class = CustomPagination

    permission_classes = (permissions.IsAuthenticated, )


class BulletinDetailView(RetrieveAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^code', '^title']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['begin_time']
    ordering = ['-begin_time']

    pagination_class = NotPaginatedSetPagination 
    permission_classes = (permissions.IsAuthenticated, )


class BulletinCreateView(CreateAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BulletinUpdateView(UpdateAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BulletinDeleteView(DestroyAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (permissions.IsAuthenticated, )

class BulletinSendView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Bulletin.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bulletin = self.get_object(pk)
        cblt.send_bulletin(bulletin)
        serializer_class = BulletinSerializer
        return Response({'message': str(cblt.msg) })

    def put(self, request, pk, format=None):
        bulletin = self.get_object(pk)
        serializer_class = BulletinSerializer(bulletin, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bulletin = self.get_object(pk)
        bulletin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)