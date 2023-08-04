from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from mailings.serializers import MailingSerializer
from mailings.models import Mailing


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Mailing.objects.all()
