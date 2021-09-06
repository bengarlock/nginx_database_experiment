from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class ResyGroup(models.Model):
    name = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=3000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ResyRestaurant(models.Model):
    name = models.CharField(max_length=3000, blank=True)
    resy_id = models.CharField(max_length=1000, blank=True)
    neighborhood = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=3000, blank=True, null=True)
    address = models.CharField(max_length=3000, blank=True, null=True)
    active = models.BooleanField(default=True)
    group = models.ForeignKey(ResyGroup, related_name="restaurants", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ResyTotalCount(models.Model):
    total_count = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class YelpRestaurant(models.Model):
    restaurant_name = models.CharField(max_length=3000, blank=True)
    yelp_id = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=3000, blank=True, null=True)
    address = models.CharField(max_length=3000, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class YelpTotals(models.Model):
    total_count = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
