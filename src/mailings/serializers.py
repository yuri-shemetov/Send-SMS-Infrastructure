from rest_framework import serializers
from mailings import models


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mailing
        fields = [
            "first_name",
            "last_name",
            "patronymic",
            "phone",
            "email",
            "created_at",
            "updated_at",
        ]
