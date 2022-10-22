from django.db import models

# Create your models here.


class Book(models.Model):
    book_id = models.CharField(max_length=500, unique=True, default='-')
    title = models.CharField(max_length=1000, default='')
    author = models.CharField(max_length=1000, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    description = models.CharField(max_length=5000, default='')
    language = models.CharField(max_length=30, default='')
    isbn = models.CharField(max_length=13, default='')
    genres = models.CharField(max_length=500, default='')
    characters = models.CharField(max_length=1000, default='')
    book_format = models.CharField(max_length=30, default='')
    edition = models.CharField(max_length=120, default='')
    pages = models.SmallIntegerField(default=0)
    publisher = models.CharField(max_length=120, default='')
    publish_date = models.CharField(max_length=30, default='')
    first_publish_date = models.CharField(max_length=30, default='')
    awards = models.CharField(max_length=1000, default='[]')
    num_ratings = models.CharField(max_length=7, default='-')
    ratings_by_stars = models.CharField(max_length=120, default='[]')
    liked_percent = models.CharField(max_length=3, default='')
    setting = models.CharField(max_length=500, default='')
    cover_img = models.URLField(default='')
    bbe_score = models.IntegerField(default=0)
    bbe_votes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=500, default='')
    hints = models.CharField(max_length=500, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.phone_num
