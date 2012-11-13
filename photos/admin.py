from photos.models import (Photo, Collection, PublicCollection,
                           PhotoToCollection)
from django.contrib import admin
from django.core.urlresolvers import reverse


class CollectionPhotosInline(admin.TabularInline):
    model = Collection.photos.through


class PublicCollectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'description', 'published')}),
        ('Cover photo settings', {'fields': ('cover_image',
                                             'cover_image_width',
                                             'cover_image_height'),
                                  'classes': ['collapse']}),
        ('Member photo settings', {'fields': ('member_image_width',
                                              'member_image_height'),
                                   'classes': ['collapse']}))
    inlines = [CollectionPhotosInline,]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_display', 'collection_list')
    fieldsets = (
        (None, {'fields': ('image', 'collections')}),
        ('Dimensions', {'fields': ('width', 'height'),
                        'classes': ['collapse']}),
        ('Link to original image', {'fields': ('original',),
                                    'classes': ['collapse']})
    )
    filter_horizontal = ('collections',)

    def image_display(self, instance):
        img_template = '<img src="%s" width="100px" height="100px"></img>'
        return img_template %  (unicode(instance.image.url),)

    image_display.short_description = "Photo"
    image_display.allow_tags = True

    def collection_list(self, instance):
        link_template = '<a href="%s">%s</a>'
        return ', '.join(
            link_template % (
                reverse('admin:photos_publiccollection_change',
                    args=(c['id'],)
                ),
                c['name']
            ) for c in instance.collections.values())
    
    collection_list.short_description = "Collections"
    collection_list.allow_tags = True

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PublicCollection, PublicCollectionAdmin)
