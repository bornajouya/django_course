from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class MyUser(User):
    cover = models.ImageField(upload_to="cover", blank=True, null=True)
    phone_number = models.CharField(max_length=10, default="", blank=True, null=True)

    def __str__(self):
        return self.username
