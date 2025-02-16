from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default="Неизвестный автор"
    )

    publish = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    message = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return self.message
