# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Job.description'
        db.add_column('job_postings_job', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Job.hours_description'
        db.add_column('job_postings_job', 'hours_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Job.description'
        db.delete_column('job_postings_job', 'description')

        # Deleting field 'Job.hours_description'
        db.delete_column('job_postings_job', 'hours_description')


    models = {
        'job_postings.job': {
            'Meta': {'object_name': 'Job'},
            'closing_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'contract_length': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'extension_possible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hours_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hours_per_week': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['job_postings.Location']", 'symmetrical': 'False'}),
            'payscale_end': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'payscale_period': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'payscale_start': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'positions_available': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'qualifications': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'union': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'job_postings.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['job_postings']