from django.db import models


class TestBase(models.Model):
    name = models.TextField(blank=False, null=False, default='хуи')
    number = models.IntegerField(blank=False, null=False, default=0)

# Create your models here.
