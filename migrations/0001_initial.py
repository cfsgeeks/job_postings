# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('job_postings_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('job_postings', ['Location'])

        # Adding model 'Job'
        db.create_table('job_postings_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length='1')),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('closing_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('contract_length', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('extension_possible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('union', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('positions_available', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('qualifications', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('requirements', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('payscale_start', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('payscale_end', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('payscale_period', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('hours_per_week', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('job_postings', ['Job'])

        # Adding M2M table for field location on 'Job'
        m2m_table_name = db.shorten_name('job_postings_job_location')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm['job_postings.job'], null=False)),
            ('location', models.ForeignKey(orm['job_postings.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'location_id'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('job_postings_location')

        # Deleting model 'Job'
        db.delete_table('job_postings_job')

        # Removing M2M table for field location on 'Job'
        db.delete_table(db.shorten_name('job_postings_job_location'))


    models = {
        'job_postings.job': {
            'Meta': {'object_name': 'Job'},
            'closing_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'contract_length': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'extension_possible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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