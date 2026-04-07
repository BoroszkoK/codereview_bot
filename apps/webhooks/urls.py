from django.urls import path

from .views import GitHubWebhookView

app_name = "webhooks"

urlpatterns = [
    path("github/", GitHubWebhookView.as_view(), name="github-webhook"),
]
