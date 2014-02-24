# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SpecialOffer.is_week_offer'
        db.add_column(u'sections_specialoffer', 'is_week_offer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'SpecialOffer.short_description'
        db.alter_column(u'sections_specialoffer', 'short_description', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):
        # Deleting field 'SpecialOffer.is_week_offer'
        db.delete_column(u'sections_specialoffer', 'is_week_offer')


        # Changing field 'SpecialOffer.short_description'
        db.alter_column(u'sections_specialoffer', 'short_description', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        u'sections.specialoffer': {
            'Meta': {'object_name': 'SpecialOffer'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_week_offer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'short_description': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sections']