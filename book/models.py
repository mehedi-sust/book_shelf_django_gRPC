from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_published = models.IntegerField()
    genres = models.JSONField(default=list)

    class Meta:
        ordering = ["id"]
