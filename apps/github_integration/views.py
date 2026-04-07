from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import GitHubRepository
from .serializers import GitHubRepositorySerializer


class GitHubRepositoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for repositories that have installed the bot."""

    queryset = GitHubRepository.objects.filter(active=True)
    serializer_class = GitHubRepositorySerializer
    permission_classes = [IsAuthenticated]
