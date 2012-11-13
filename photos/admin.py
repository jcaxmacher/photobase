from photos.models import (Photo, Collection, PublicCollection,
                           PhotoToCollection)
from django.contrib import admin

class CollectionInline(admin.TabularInline):
    model = Collection.photos.through

class PublicCollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionInline,]

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'width', 'height', 'original',
        'collections')}),)
    filter_horizontal = ('collections',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PublicCollection, PublicCollectionAdmin)
