from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from mailings.services import sending_router
from mailings.serializers import MailingSerializer
from mailings.models import Mailing, MailingText


class CreateMailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Mailing.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            sending_router(
                mailing_text=serializer.get("mailing_text"),
                clients=serializer.get("clients"),
                send_date=serializer.get("send_date"),
            )
            serializer.save()
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response({"saved": False}, status=status.HTTP_400_BAD_REQUEST)