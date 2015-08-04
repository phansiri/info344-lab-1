from django.db import models

class url(models.Model):
    originalUrl = models.CharField(max_length=1000)
    finalUrl = models.CharField(max_length=1000)
    httpStatusCode = models.CharField(max_length=5)
    pageTitle = models.CharField(max_length=400)

    def submit(self):
        self.save()

    def __str__(self):
        return self.finalUrl
