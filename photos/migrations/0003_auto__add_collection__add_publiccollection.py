# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collection'
        db.create_table('photos_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cover_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'])),
            ('cover_image_width', self.gf('django.db.models.fields.IntegerField')()),
            ('cover_image_height', self.gf('django.db.models.fields.IntegerField')()),
            ('member_image_width', self.gf('django.db.models.fields.IntegerField')()),
            ('member_image_height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('photos', ['Collection'])

        # Adding model 'PublicCollection'
        db.create_table('photos_publiccollection', (
            ('collection_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['photos.Collection'], unique=True, primary_key=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('photos', ['PublicCollection'])


    def backwards(self, orm):
        # Deleting model 'Collection'
        db.delete_table('photos_collection')

        # Deleting model 'PublicCollection'
        db.delete_table('photos_publiccollection')


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
        'photos.publiccollection': {
            'Meta': {'object_name': 'PublicCollection', '_ormbases': ['photos.Collection']},
            'collection_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['photos.Collection']", 'unique': 'True', 'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['photos']