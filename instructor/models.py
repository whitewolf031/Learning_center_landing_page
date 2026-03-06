from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    bio = models.TextField()

    image = models.URLField()

    skills = models.JSONField(blank=True, null=True)
    rating = models.FloatField(default=0)

    students = models.IntegerField(default=0)
    experience = models.TextField()

    achievements = models.JSONField(blank=True, null=True)

    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
