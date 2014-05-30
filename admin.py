from django.contrib import admin
from django import forms
from job_postings.models import Job, Location

class JobAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'mceEditor'})}, }

admin.site.register(Job)
admin.site.register(Location)