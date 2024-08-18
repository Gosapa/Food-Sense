from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    diseases = models.JSONField(default=list, blank=True)
    allergies = models.JSONField(default=list, blank=True)
    favorites = models.JSONField(default=list, blank=True)

    def __str__(self):
        return "Profile of `" + self.user.first_name + "`"
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()