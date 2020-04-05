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


class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class StateDetailView(RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
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
