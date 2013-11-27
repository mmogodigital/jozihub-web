# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HeardAboutChoice.order'
        db.add_column(u'root_heardaboutchoice', 'order',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TypeOfSpaceRequiredChoice.order'
        db.add_column(u'root_typeofspacerequiredchoice', 'order',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EventHostingChoice.order'
        db.add_column(u'root_eventhostingchoice', 'order',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PartnerChoice.order'
        db.add_column(u'root_partnerchoice', 'order',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HeardAboutChoice.order'
        db.delete_column(u'root_heardaboutchoice', 'order')

        # Deleting field 'TypeOfSpaceRequiredChoice.order'
        db.delete_column(u'root_typeofspacerequiredchoice', 'order')

        # Deleting field 'EventHostingChoice.order'
        db.delete_column(u'root_eventhostingchoice', 'order')

        # Deleting field 'PartnerChoice.order'
        db.delete_column(u'root_partnerchoice', 'order')


    models = {
        u'root.application': {
            'Meta': {'object_name': 'Application'},
            'about_you': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_your_organisation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'affiliation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aims_to_get_from_jozihub': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'background_and_expertise': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'become_a_partner_or_funder': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['root.PartnerChoice']", 'null': 'True', 'blank': 'True'}),
            'become_a_partner_or_funder_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'educational_background': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'events_interesting_in_hosting': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['root.EventHostingChoice']", 'null': 'True', 'blank': 'True'}),
            'events_interesting_in_hosting_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_of_expertise': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_of_expertise_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'happy_with_the_price': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'heard_about_from': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['root.HeardAboutChoice']", 'null': 'True', 'blank': 'True'}),
            'heard_about_from_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'how_can_you_contribute_to_jozihub': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information_about_jozihub': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mentoring_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'partnership_expectation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'required_from_us': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'submit_reason': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type_of_space_required': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['root.TypeOfSpaceRequiredChoice']", 'null': 'True', 'blank': 'True'}),
            'what_can_you_offer_as_a_mentor': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'what_do_you_aim_to_achieve': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'when_to_get_access': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'when_to_host_event': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'root.eventhostingchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'EventHostingChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'root.heardaboutchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'HeardAboutChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'root.partnerchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'PartnerChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'root.typeofspacerequiredchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeOfSpaceRequiredChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['root']