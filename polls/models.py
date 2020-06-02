from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=40)
    mobile = models.IntegerField()
    password = models.CharField(max_length=12)


class sport(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name