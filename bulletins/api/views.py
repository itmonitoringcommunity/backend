# from rest_framework import viewsets

# class BulletinViewSet(viewsets.ModelViewSet):
#     serializer_class = BulletinSerializer
#     queryset = Bulletin.objects.all()

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from bulletins.models import Bulletin
from .serializers import BulletinSerializer


class BulletinListView(ListAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BulletinDetailView(RetrieveAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
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

class BulletinSendView(RetrieveAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (permissions.IsAuthenticated, )