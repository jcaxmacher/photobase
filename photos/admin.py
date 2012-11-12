from photos.models import (Photo, PublicCollection, PhotoToCollection)
from django.contrib import admin

admin.site.register(Photo)
admin.site.register(PublicCollection)
admin.site.register(PhotoToCollection)
