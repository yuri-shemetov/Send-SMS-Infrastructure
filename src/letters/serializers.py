from rest_framework import serializers
from letters import models


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Letter
        fields = [
            "title",
            "text",
        ]
