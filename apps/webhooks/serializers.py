from rest_framework import serializers

from .models import WebhookEvent


class WebhookEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookEvent
        fields = "__all__"
        read_only_fields = ["received_at"]
