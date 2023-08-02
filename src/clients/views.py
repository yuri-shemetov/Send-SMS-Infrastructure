from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from clients.serializers import ClientSerializer
from clients.models import Client


class PageModelViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Client.objects.all()
