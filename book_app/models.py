from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    the_top_seller = models.BooleanField()
    author = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return f"{self.title} - {self.rating}%"