from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class GitHubWebhookView(APIView):
    """Receive and enqueue incoming GitHub webhook events."""

    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        # TODO: validate X-Hub-Signature-256 header against GITHUB_WEBHOOK_SECRET
        # TODO: persist WebhookEvent and enqueue Celery processing task
        return Response({"status": "queued"}, status=status.HTTP_202_ACCEPTED)
