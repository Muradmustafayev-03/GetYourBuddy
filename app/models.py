from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Profile(User):
    nickname = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='static/img')
    birthdate = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)
