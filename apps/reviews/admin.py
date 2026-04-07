from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["repository", "pull_request_number", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["repository"]
    readonly_fields = ["created_at", "updated_at"]
