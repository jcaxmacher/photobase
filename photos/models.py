from django.db import models
from django.conf import settings

class Photo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(max_length=300, upload_to='images/')
