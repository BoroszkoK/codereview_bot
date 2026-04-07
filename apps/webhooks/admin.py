from django.contrib import admin

from .models import WebhookEvent


@admin.register(WebhookEvent)
class WebhookEventAdmin(admin.ModelAdmin):
    list_display = ["event_type", "delivery_id", "received_at", "processed"]
    list_filter = ["event_type", "processed"]
    readonly_fields = ["received_at"]
    search_fields = ["delivery_id", "event_type"]
