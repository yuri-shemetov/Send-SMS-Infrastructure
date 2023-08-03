from rest_framework import serializers
from mailings import models


class MailingSerializer(serializers.ModelSerializer):
    # mailing_text = serializers.SlugRelatedField(slug_field="title", read_only=False)
    class Meta:
        model = models.Mailing
        fields = [
            "clients",
            "mailing_text",
        ]
