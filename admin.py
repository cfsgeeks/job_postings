from django.contrib import admin
from job_postings.models import Job, Location

class JobAdmin(admin.ModelAdmin):
    list_display = ("title","location","closing_date")

admin.site.register(Job,JobAdmin)
admin.site.register(Location)