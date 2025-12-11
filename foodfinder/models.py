from django.db import models
from django.urls import reverse
from django.conf import settings
from foodfinder.models import *
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default="password")
    def __str__(self):
        base = f"{self.first_name} {self.last_name}"
        return f"{base}"

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=30)
    restaurant_location = models.CharField(max_length=30)
    restaurant_latitude = models.FloatField()
    restaurant_longitude = models.FloatField()
    restaurant_price = models.IntegerField()
    avg_rating = models.FloatField()
    def __str__(self):
        base = f"{self.restaurant_name}, {self.restaurant_location}"
        return f"{base}"
    def get_absolute_url(self):
        return reverse('restaurant-detail-url',
                       kwargs={'primary_key': self.pk}
                       )
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_user_name')
    # user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='review_user_name')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='review_restaurant_name')

