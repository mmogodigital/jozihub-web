# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'startup_companies'
        db.create_table(u'startups_startup_companies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('short_descriptor', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('long_descriptor', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('founder_photographs', self.gf('django.db.models.fields.TextField')(max_length=120, null=True, blank=True)),
            ('Link_to_their_website', self.gf('django.db.models.fields.TextField')(max_length=120, null=True, blank=True)),
            ('social_media_profiles', self.gf('django.db.models.fields.TextField')(max_length=120, null=True, blank=True)),
            ('contact_details', self.gf('django.db.models.fields.TextField')(max_length=120, null=True, blank=True)),
            ('rel_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'startups', ['startup_companies'])


    def backwards(self, orm):
        # Deleting model 'startup_companies'
        db.delete_table(u'startups_startup_companies')


    models = {
        u'startups.startup_companies': {
            'Link_to_their_website': ('django.db.models.fields.TextField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'startup_companies'},
            'contact_details': ('django.db.models.fields.TextField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'founder_photographs': ('django.db.models.fields.TextField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'long_descriptor': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'rel_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'short_descriptor': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'social_media_profiles': ('django.db.models.fields.TextField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['startups']