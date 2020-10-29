from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    photo = models.URLField()
    website = models.URLField()
    description = models.TextField()