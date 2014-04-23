from django.contrib import admin
from job_postings.models import SalariedJob,NonSalariedJob

admin.site.register(SalariedJob)
admin.site.register(NonSalariedJob)