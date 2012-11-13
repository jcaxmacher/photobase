from photos.models import (Photo, Collection, PublicCollection,
                           PhotoToCollection)
from django.contrib import admin

class CollectionPhotosInline(admin.TabularInline):
    model = Collection.photos.through

class PublicCollectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'description', 'published')}),
        ('Cover photo settings', {'fields': ('cover_image',
        'cover_image_width', 'cover_image_height')}),
        ('Member photo settings', {'fields': ('member_image_width',
        'member_image_height')}))
    inlines = [CollectionPhotosInline,]

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'collections')}),
        ('Dimensions', {'fields': ('width', 'height')}),
        ('Link to original image', {'fields': ('original',)})
    )
    filter_horizontal = ('collections',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PublicCollection, PublicCollectionAdmin)
