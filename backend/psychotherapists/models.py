from django.db import models


class Psychotherapist(models.Model):
    date_loaded = models.DateField(auto_now=True)
    data = models.JSONField()
