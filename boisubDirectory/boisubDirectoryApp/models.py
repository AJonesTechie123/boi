from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author_first_Name = models.CharField(max_length=200, unique=True)
    author_last_Name = models.CharField(max_length=200, unique=True)
