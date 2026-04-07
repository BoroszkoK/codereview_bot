from django.db import models


class WebhookEvent(models.Model):
    """Raw GitHub webhook payload received from the API."""

    event_type = models.CharField(max_length=100)
    delivery_id = models.CharField(max_length=100, unique=True)
    payload = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-received_at"]

    def __str__(self) -> str:
        return f"{self.event_type} ({self.delivery_id})"
