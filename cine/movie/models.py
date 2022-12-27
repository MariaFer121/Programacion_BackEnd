from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        null=True
    )


class Movie(models.Model):
    is_premier = models.BooleanField()
    title = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title