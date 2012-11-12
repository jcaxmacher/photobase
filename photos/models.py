from django.db import models
from django.conf import settings

class Photo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(max_length=300, upload_to='images/')

class Collection(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ForeignKey('Photo')
    cover_image_width = models.IntegerField()
    cover_image_height = models.IntegerField()
    member_image_width = models.IntegerField()
    member_image_height = models.IntegerField()

class PublicCollection(Collection):
    published = models.BooleanField()

class PhotoToCollection(models.Model):
    collection = models.ForeignKey('Collection')
    photo = models.ForeignKey('Photo')
