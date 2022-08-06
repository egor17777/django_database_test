import imp
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):

    THE_ORIGIN_OF_THE_WRITER =[
        ("USA", "UNITED STATES"),
        ("EUR", "EUROPE"),
        ("UKR", "UKRINE")
    ]

    title = models.CharField(max_length=70)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(default=2000, validators=[MinValueValidator(1)])
    the_top_seller = models.BooleanField()
    author = models.CharField(max_length=100, null=True, blank= True)
    slug = models.SlugField(default='',null=False)
    origin = models.CharField(max_length=3, choices= THE_ORIGIN_OF_THE_WRITER, default="UKR")


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book, self).save(*args, **kwargs)



    def __str__(self) -> str:
        return f"{self.title} - {self.rating}%"

    def get_url(self):
        return reverse('book-url', args=[self.slug])