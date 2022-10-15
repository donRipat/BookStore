from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    genres = models.CharField(max_length=500)
    rating = models.CharField(max_length=4)
    price = models.CharField(max_length=10)
    img = models.CharField(max_length=150)
    pages_num = models.SmallIntegerField()

    def __str__(self):
        return self.title
