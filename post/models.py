from django.db import models
from django.contrib.auth.models import User

from about.models import UsefulModel


class CommentsModel(UsefulModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description}/{self.is_pinned}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    @property
    def author_name(self):
        return self.user.get_full_name()
