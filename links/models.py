from django.db import models

# Create your models here.


class Link(models.Model):
    url = models.URLField()
    descritpion = models.TextField(blank=True)

    def __str__(self):
        return self.url
