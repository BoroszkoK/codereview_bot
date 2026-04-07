from django.contrib import admin

from .models import GitHubRepository


@admin.register(GitHubRepository)
class GitHubRepositoryAdmin(admin.ModelAdmin):
    list_display = ["full_name", "installation_id", "active", "created_at"]
    list_filter = ["active"]
    search_fields = ["owner", "name"]
    readonly_fields = ["created_at"]
