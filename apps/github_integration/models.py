from django.db import models


class GitHubRepository(models.Model):
    """A GitHub repository that has installed the CodeReview Bot."""

    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    installation_id = models.BigIntegerField(unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["owner", "name"]
        unique_together = [["owner", "name"]]

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.name}"

    def __str__(self) -> str:
        return self.full_name
