from rest_framework import serializers
from clients import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = [
            "first_name",
            "last_name",
            "patronymic",
            "phone",
            "email",
            "created_at",
            "updated_at",
        ]
