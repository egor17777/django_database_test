import imp
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class PublishingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()



    def __str__(self) -> str:
        return f"{self.floor}  {self.number}"


class Hero(models.Model):
    MALE = "M"
    FEMALE = "F"
    THE_GENDER =[
        (MALE, "Male"),
        (FEMALE, "Female")
    ]
    name_hero = models.CharField(max_length=40, null=True, blank= True)
    type_hero = models.CharField(max_length=40, null=True, blank= True)
    age_hero = models.IntegerField(null=True, blank= True)
    gender = models.CharField(max_length=1, choices= THE_GENDER, default="M")

    def get_url(self):
        return reverse("hero-url", args=[self.id])


    def __str__(self) -> str:
        if self.gender == self.MALE:
            return f"She is hero: {self.name_hero}  {self.type_hero}"
        if self.gender == self.FEMALE:
            return f"He is hero: {self.name_hero}  {self.type_hero}"


class Author(models.Model):
    first_name = models.CharField(max_length=40, null=True, blank= True)
    last_name = models.CharField(max_length=40, null=True, blank= True)
    author_mail = models.EmailField(null=True, blank= True)
    publishing = models.OneToOneField(PublishingRoom, on_delete=models.SET_NULL, null = True, blank= True)


    def get_url(self):
        return reverse("author-url", args=[self.id])

    def __str__(self) -> str:
        return f"{self.first_name}  {self.last_name}"




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
    slug = models.SlugField(default='',null=False)
    origin = models.CharField(max_length=3, choices= THE_ORIGIN_OF_THE_WRITER, default="UKR")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    hero = models.ManyToManyField(Hero)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book, self).save(*args, **kwargs)



    def __str__(self) -> str:
        return f"{self.title} - {self.rating}%"

    def get_url(self):
        return reverse('book-url', args=[self.slug])