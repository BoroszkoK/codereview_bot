from rest_framework import serializers

from .models import GitHubRepository


class GitHubRepositorySerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = GitHubRepository
        fields = "__all__"
        read_only_fields = ["created_at"]
