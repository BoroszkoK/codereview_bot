from django.db import models


class Review(models.Model):
    """AI-generated code review for a pull request."""

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    repository = models.CharField(max_length=255)
    pull_request_number = models.PositiveIntegerField()
    pull_request_url = models.URLField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    review_body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = [["repository", "pull_request_number"]]

    def __str__(self) -> str:
        return f"Review for {self.repository}#{self.pull_request_number}"
