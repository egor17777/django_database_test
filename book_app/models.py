from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    year = models.IntegerField(default=2000)
    the_top_seller = models.BooleanField()
    author = models.CharField(max_length=100, null=True)
    slug = models.SlugField(default='',null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book, self).save(*args, **kwargs)



    def __str__(self) -> str:
        return f"{self.title} - {self.rating}%"

    def get_url(self):
        return reverse('book-url', args=[self.slug])