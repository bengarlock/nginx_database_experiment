from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    date = models.DateField()
    restaurant_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Guest(models.Model):
    first_name = models.TextField(default='', max_length=500, blank=True)
    last_name = models.TextField(default='', max_length=500, blank=True)
    phone_number = models.TextField(default='', blank=True)
    guest_notes = models.TextField(default='', blank=True)
    slot = ArrayField(models.CharField(max_length=15), default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)


class Restaurant(models.Model):
    name = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Status(models.Model):
    color = models.CharField(default='#fff', max_length=1000)
    name = models.CharField(default='', max_length=1000)
    status_type = models.CharField(default='confirmation', max_length=1000)
    order = models.IntegerField(default=0)
    display_floor = models.BooleanField(default=True)


class Slot(models.Model):
    booked = models.BooleanField(default=False)
    time = models.TextField(default="5:00 PM")
    party_size = models.IntegerField(default=0)
    reservation_notes = models.TextField(blank=True)
    book = models.ForeignKey(Book, related_name="slots", on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name="guest", on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, related_name="status", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Floor(models.Model):
    book = models.ForeignKey(Book, related_name="floors", on_delete=models.SET_NULL, null=True)
    name = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class TableManager(models.Manager):
    def get_by_natural_key(self, width, height):
        return self.get(width=width, height=height)

class Table(models.Model):
    floor = models.ForeignKey(Floor, related_name='tables', on_delete=models.CASCADE, null=True)
    class_name = models.TextField(default="two-top-horizontal")
    left = models.TextField(default="0px")
    top = models.TextField(default="0px")
    name = models.TextField(blank=True)
    status = models.TextField(default='open')
    width = models.TextField(default='50px')
    height = models.TextField(default='50px')
    background_color = models.TextField(default='#9b9b9b')
    border = models.TextField(default='"2px solid gray"')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    objects = TableManager()

    class Meta:
        unique_together = [['width', 'height']]



