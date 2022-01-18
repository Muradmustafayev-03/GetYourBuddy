import random
import time

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(User):
    nickname = models.CharField(max_length=150)
    user_id = str(time.time()) + str(random.randint(0, 1000))
    photo = models.ImageField()
    birthdate = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)
