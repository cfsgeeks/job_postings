from django.contrib import admin
from job_postings.models import Job, Location

class LocationAdmin(admin.ModelAdmin):
	def get_model_perms(self,request):
		return {}

admin.site.register(Job)
admin.site.register(Location,LocationAdmin)