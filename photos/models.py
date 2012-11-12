from django.db import models
from django.conf import settings

class Photo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(max_length=300, upload_to='images/')
    width = models.IntegerField(blank=True, null=True, db_index=True)
    height = models.IntegerField(blank=True, null=True, db_index=True)
    original = models.ForeignKey('self', blank=True, null=True, db_index=True)

class Collection(models.Model):
    name = models.CharField(max_length=255, blank=True, db_index=True)
    description = models.TextField(blank=True)
    cover_image = models.ForeignKey('Photo', related_name='cover_image')
    cover_image_width = models.IntegerField()
    cover_image_height = models.IntegerField()
    member_image_width = models.IntegerField()
    member_image_height = models.IntegerField()
    photos = models.ManyToManyField(Photo, through='PhotoToCollection')

class PublicCollection(Collection):
    published = models.BooleanField(db_index=True)

class PhotoToCollection(models.Model):
    collection = models.ForeignKey('Collection', db_index=True)
    photo = models.ForeignKey('Photo', db_index=True)
