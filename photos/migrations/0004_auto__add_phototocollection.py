# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhotoToCollection'
        db.create_table('photos_phototocollection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Collection'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'])),
        ))
        db.send_create_signal('photos', ['PhotoToCollection'])


    def backwards(self, orm):
        # Deleting model 'PhotoToCollection'
        db.delete_table('photos_phototocollection')


    models = {
        'photos.collection': {
            'Meta': {'object_name': 'Collection'},
            'cover_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"}),
            'cover_image_height': ('django.db.models.fields.IntegerField', [], {}),
            'cover_image_width': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_image_height': ('django.db.models.fields.IntegerField', [], {}),
            'member_image_width': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '300'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'photos.phototocollection': {
            'Meta': {'object_name': 'PhotoToCollection'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Collection']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"})
        },
        'photos.publiccollection': {
            'Meta': {'object_name': 'PublicCollection', '_ormbases': ['photos.Collection']},
            'collection_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['photos.Collection']", 'unique': 'True', 'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['photos']