# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table('photos_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=300)),
        ))
        db.send_create_signal('photos', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table('photos_photo')


    models = {
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '300'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['photos']