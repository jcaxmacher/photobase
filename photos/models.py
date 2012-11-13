from django.db import models
from django.conf import settings


class Photo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(max_length=300, upload_to='images/')
    width = models.IntegerField(blank=True, null=True, db_index=True)
    height = models.IntegerField(blank=True, null=True, db_index=True)
    original = models.ForeignKey('self', blank=True, null=True, db_index=True)
    collections = models.ManyToManyField('Collection',
        through='PhotoToCollection')

    def __unicode__(self):
        return unicode(self.image.file)


class Collection(models.Model):
    name = models.CharField(max_length=255, blank=True, db_index=True)
    description = models.TextField(blank=True)
    cover_image = models.ForeignKey('Photo', related_name='cover_image')
    cover_image_width = models.IntegerField()
    cover_image_height = models.IntegerField()
    member_image_width = models.IntegerField()
    member_image_height = models.IntegerField()
    photos = models.ManyToManyField('Photo', through='PhotoToCollection')

    def __unicode__(self):
        return self.name

class PublicCollection(Collection):
    published = models.BooleanField(db_index=True)

class PhotoToCollection(models.Model):
    collection = models.ForeignKey('Collection', db_index=True)
    photo = models.ForeignKey('Photo', db_index=True)

    def __unicode__(self):
        return 'Photo({0}), Collection({1})'.format(
            self.photo.id, self.collection.id
        )

# Trick to get the filter_horizonal widget to display for collection
# selection on the Photo model add page in the django admin
PhotoToCollection._meta.auto_created = True
