from django.db import models


class Local(models.Model):
    _DATABASE = 'default'
    name = models.CharField(max_length=50)
    data = models.JSONField()


class Remote(models.Model):
    _DATABASE = 'remote'
    name = models.CharField(max_length=50)
    data = models.JSONField()