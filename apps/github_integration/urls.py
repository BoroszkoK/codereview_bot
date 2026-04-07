from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GitHubRepositoryViewSet

app_name = "github_integration"

router = DefaultRouter()
router.register("repositories", GitHubRepositoryViewSet, basename="repository")

urlpatterns = [
    path("", include(router.urls)),
]
