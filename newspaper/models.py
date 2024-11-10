from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField()
    topics = models.ManyToManyField("Topic", related_name="newspaper")
    publishers = models.ManyToManyField("Redactor", related_name="newspaper")

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Redactor"
        verbose_name_plural = "Redactors"
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return f"{self.username} {self.years_of_experience}"
