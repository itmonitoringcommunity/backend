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


class BTypeListView(ListAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BTypeDetailView(RetrieveAPIView):
    queryset = BType.objects.all()
    serializer_class = BTypeSerializer
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
