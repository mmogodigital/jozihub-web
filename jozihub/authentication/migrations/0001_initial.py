# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HeardAboutChoice'
        db.create_table(u'authentication_heardaboutchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'authentication', ['HeardAboutChoice'])

        # Adding model 'EventHostingChoice'
        db.create_table(u'authentication_eventhostingchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'authentication', ['EventHostingChoice'])

        # Adding model 'TypeOfSpaceRequiredChoice'
        db.create_table(u'authentication_typeofspacerequiredchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'authentication', ['TypeOfSpaceRequiredChoice'])

        # Adding model 'PartnerChoice'
        db.create_table(u'authentication_partnerchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'authentication', ['PartnerChoice'])

        # Adding model 'EndUser'
        db.create_table(u'authentication_enduser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='enduser_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('username', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, unique=True, null=True, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('street_address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zip_postal_code', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('web_address', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('is_regular_user', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_console_user', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('heard_about_from_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('affiliation', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('submit_reason', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('information_about_jozihub', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('educational_background', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_you', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('events_interested_in_hosting_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('when_to_host_event', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('required_from_us', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('how_can_you_contribute_to_jozihub', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('aims_to_get_from_jozihub', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('when_to_get_access', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('happy_with_the_price', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
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
        db.send_create_signal(u'authentication', ['EndUser'])

        # Adding M2M table for field groups on 'EndUser'
        m2m_table_name = db.shorten_name(u'authentication_enduser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enduser', models.ForeignKey(orm[u'authentication.enduser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enduser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'EndUser'
        m2m_table_name = db.shorten_name(u'authentication_enduser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enduser', models.ForeignKey(orm[u'authentication.enduser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enduser_id', 'permission_id'])

        # Adding M2M table for field heard_about_from on 'EndUser'
        m2m_table_name = db.shorten_name(u'authentication_enduser_heard_about_from')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enduser', models.ForeignKey(orm[u'authentication.enduser'], null=False)),
            ('heardaboutchoice', models.ForeignKey(orm[u'authentication.heardaboutchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enduser_id', 'heardaboutchoice_id'])

        # Adding M2M table for field events_interested_in_hosting on 'EndUser'
        m2m_table_name = db.shorten_name(u'authentication_enduser_events_interested_in_hosting')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enduser', models.ForeignKey(orm[u'authentication.enduser'], null=False)),
            ('eventhostingchoice', models.ForeignKey(orm[u'authentication.eventhostingchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enduser_id', 'eventhostingchoice_id'])

        # Adding M2M table for field type_of_space_required on 'EndUser'
        m2m_table_name = db.shorten_name(u'authentication_enduser_type_of_space_required')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enduser', models.ForeignKey(orm[u'authentication.enduser'], null=False)),
            ('typeofspacerequiredchoice', models.ForeignKey(orm[u'authentication.typeofspacerequiredchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enduser_id', 'typeofspacerequiredchoice_id'])

        # Adding M2M table for field become_a_partner_or_funder on 'EndUser'
        m2m_table_name = db.shorten_name(u'authentication_enduser_become_a_partner_or_funder')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enduser', models.ForeignKey(orm[u'authentication.enduser'], null=False)),
            ('partnerchoice', models.ForeignKey(orm[u'authentication.partnerchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enduser_id', 'partnerchoice_id'])

        # Adding model 'ProjectRegistrationProfile'
        db.create_table(u'authentication_projectregistrationprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authentication.EndUser'], unique=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'authentication', ['ProjectRegistrationProfile'])


    def backwards(self, orm):
        # Deleting model 'HeardAboutChoice'
        db.delete_table(u'authentication_heardaboutchoice')

        # Deleting model 'EventHostingChoice'
        db.delete_table(u'authentication_eventhostingchoice')

        # Deleting model 'TypeOfSpaceRequiredChoice'
        db.delete_table(u'authentication_typeofspacerequiredchoice')

        # Deleting model 'PartnerChoice'
        db.delete_table(u'authentication_partnerchoice')

        # Deleting model 'EndUser'
        db.delete_table(u'authentication_enduser')

        # Removing M2M table for field groups on 'EndUser'
        db.delete_table(db.shorten_name(u'authentication_enduser_groups'))

        # Removing M2M table for field user_permissions on 'EndUser'
        db.delete_table(db.shorten_name(u'authentication_enduser_user_permissions'))

        # Removing M2M table for field heard_about_from on 'EndUser'
        db.delete_table(db.shorten_name(u'authentication_enduser_heard_about_from'))

        # Removing M2M table for field events_interested_in_hosting on 'EndUser'
        db.delete_table(db.shorten_name(u'authentication_enduser_events_interested_in_hosting'))

        # Removing M2M table for field type_of_space_required on 'EndUser'
        db.delete_table(db.shorten_name(u'authentication_enduser_type_of_space_required'))

        # Removing M2M table for field become_a_partner_or_funder on 'EndUser'
        db.delete_table(db.shorten_name(u'authentication_enduser_become_a_partner_or_funder'))

        # Deleting model 'ProjectRegistrationProfile'
        db.delete_table(u'authentication_projectregistrationprofile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'authentication.enduser': {
            'Meta': {'object_name': 'EndUser'},
            'about_you': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_your_organisation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'affiliation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aims_to_get_from_jozihub': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'background_and_expertise': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'become_a_partner_or_funder': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['authentication.PartnerChoice']", 'null': 'True', 'blank': 'True'}),
            'become_a_partner_or_funder_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'educational_background': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'enduser_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'events_interested_in_hosting': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['authentication.EventHostingChoice']", 'null': 'True', 'blank': 'True'}),
            'events_interested_in_hosting_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_of_expertise': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_of_expertise_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'happy_with_the_price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'heard_about_from': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['authentication.HeardAboutChoice']", 'null': 'True', 'blank': 'True'}),
            'heard_about_from_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'how_can_you_contribute_to_jozihub': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'information_about_jozihub': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_console_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_regular_user': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mentoring_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'partnership_expectation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'required_from_us': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'submit_reason': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'type_of_space_required': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['authentication.TypeOfSpaceRequiredChoice']", 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'web_address': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'what_can_you_offer_as_a_mentor': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'what_do_you_aim_to_achieve': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'when_to_get_access': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'when_to_host_event': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zip_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        u'authentication.eventhostingchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'EventHostingChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'authentication.heardaboutchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'HeardAboutChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'authentication.partnerchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'PartnerChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'authentication.projectregistrationprofile': {
            'Meta': {'object_name': 'ProjectRegistrationProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authentication.EndUser']", 'unique': 'True'})
        },
        u'authentication.typeofspacerequiredchoice': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeOfSpaceRequiredChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['authentication']