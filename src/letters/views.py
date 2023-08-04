from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from letters.serializers import LetterSerializer
from letters.models import Letter


class LetterModelViewSet(viewsets.ModelViewSet):
    serializer_class = LetterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Letter.objects.all()
