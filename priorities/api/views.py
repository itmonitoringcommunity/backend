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


class PriorityListView(ListAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (permissions.IsAuthenticated, )


class PriorityDetailView(RetrieveAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
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
