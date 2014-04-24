from django.contrib import admin
from job_postings.models import Job, Location

admin.site.register(Job)
admin.site.register(Location)