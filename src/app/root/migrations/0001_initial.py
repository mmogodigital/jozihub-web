# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HeardAboutChoice'
        db.create_table(u'root_heardaboutchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'root', ['HeardAboutChoice'])

        # Adding model 'EventHostingChoice'
        db.create_table(u'root_eventhostingchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'root', ['EventHostingChoice'])

        # Adding model 'TypeOfSpaceRequiredChoice'
        db.create_table(u'root_typeofspacerequiredchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'root', ['TypeOfSpaceRequiredChoice'])

        # Adding model 'PartnerChoice'
        db.create_table(u'root_partnerchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'root', ['PartnerChoice'])

        # Adding model 'Application'
        db.create_table(u'root_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('heard_about_from_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('affiliation', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('submit_reason', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('information_about_jozihub', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('educational_background', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_you', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('events_interesting_in_hosting_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('when_to_host_event', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('required_from_us', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('how_can_you_contribute_to_jozihub', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('aims_to_get_from_jozihub', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('when_to_get_access', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('happy_with_the_price', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('become_a_partner_or_funder_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('about_your_organisation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('what_do_you_aim_to_achieve', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('partnership_expectation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('field_of_expertise', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('field_of_expertise_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('background_and_expertise', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('what_can_you_offer_as_a_mentor', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mentoring_time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'root', ['Application'])

        # Adding M2M table for field heard_about_from on 'Application'
        m2m_table_name = db.shorten_name(u'root_application_heard_about_from')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm[u'root.application'], null=False)),
            ('heardaboutchoice', models.ForeignKey(orm[u'root.heardaboutchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'heardaboutchoice_id'])

        # Adding M2M table for field events_interesting_in_hosting on 'Application'
        m2m_table_name = db.shorten_name(u'root_application_events_interesting_in_hosting')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm[u'root.application'], null=False)),
            ('eventhostingchoice', models.ForeignKey(orm[u'root.eventhostingchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'eventhostingchoice_id'])

        # Adding M2M table for field type_of_space_required on 'Application'
        m2m_table_name = db.shorten_name(u'root_application_type_of_space_required')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm[u'root.application'], null=False)),
            ('typeofspacerequiredchoice', models.ForeignKey(orm[u'root.typeofspacerequiredchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'typeofspacerequiredchoice_id'])

        # Adding M2M table for field become_a_partner_or_funder on 'Application'
        m2m_table_name = db.shorten_name(u'root_application_become_a_partner_or_funder')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm[u'root.application'], null=False)),
            ('partnerchoice', models.ForeignKey(orm[u'root.partnerchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'partnerchoice_id'])


    def backwards(self, orm):
        # Deleting model 'HeardAboutChoice'
        db.delete_table(u'root_heardaboutchoice')

        # Deleting model 'EventHostingChoice'
        db.delete_table(u'root_eventhostingchoice')

        # Deleting model 'TypeOfSpaceRequiredChoice'
        db.delete_table(u'root_typeofspacerequiredchoice')

        # Deleting model 'PartnerChoice'
        db.delete_table(u'root_partnerchoice')

        # Deleting model 'Application'
        db.delete_table(u'root_application')

        # Removing M2M table for field heard_about_from on 'Application'
        db.delete_table(db.shorten_name(u'root_application_heard_about_from'))

        # Removing M2M table for field events_interesting_in_hosting on 'Application'
        db.delete_table(db.shorten_name(u'root_application_events_interesting_in_hosting'))

        # Removing M2M table for field type_of_space_required on 'Application'
        db.delete_table(db.shorten_name(u'root_application_type_of_space_required'))

        # Removing M2M table for field become_a_partner_or_funder on 'Application'
        db.delete_table(db.shorten_name(u'root_application_become_a_partner_or_funder'))


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