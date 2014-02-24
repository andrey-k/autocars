# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Service.description'
        db.alter_column(u'sections_service', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Testimonial.text'
        db.alter_column(u'sections_testimonial', 'text', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Testimonial.author'
        db.alter_column(u'sections_testimonial', 'author', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'Worker.job_description'
        db.alter_column(u'sections_worker', 'job_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Worker.name'
        db.alter_column(u'sections_worker', 'name', self.gf('django.db.models.fields.CharField')(max_length=70))

    def backwards(self, orm):

        # Changing field 'Service.description'
        db.alter_column(u'sections_service', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Testimonial.text'
        db.alter_column(u'sections_testimonial', 'text', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Testimonial.author'
        db.alter_column(u'sections_testimonial', 'author', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Worker.job_description'
        db.alter_column(u'sections_worker', 'job_description', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Worker.name'
        db.alter_column(u'sections_worker', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'sections.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'sections.specialoffer': {
            'Meta': {'object_name': 'SpecialOffer'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_week_offer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'short_description': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sections.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'sections.worker': {
            'Meta': {'object_name': 'Worker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sections']