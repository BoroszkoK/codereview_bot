from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/webhooks/", include("apps.webhooks.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/github/", include("apps.github_integration.urls")),
]
