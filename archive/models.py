from django.db import models
from django.utils import timezone

class urlSites(models.Model):
    originalUrl = models.URLField()
    finalUrl = models.URLField(blank=True)
    httpStatusCode = models.CharField(blank=True, max_length=5)
    pageTitle = models.CharField(blank=True, max_length=400)

    def submit(self):
        self.save()

    def __str__(self):
        return self.originalUrl
