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


class MailListView(ListAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MailDetailView(RetrieveAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
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
