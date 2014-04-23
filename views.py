from django.shortcuts import render
from job_postings.models import SalariedJob, NonSalariedJob
import datetime

TODAY = datetime.date.today()

def index(request):
	salaried_jobs_list = SalariedJob.objects.filter(status='P',closing_date__gte=TODAY).order_by('-publish_date')
	nonsalaried_jobs_list = NonSalariedJob.objects.filter(status='P',closing_date__gte=TODAY).order_by('-publish_date')
	context = {'jobs':salaried_jobs_list}
	context[jobs].update(nonsalaried_jobs_list)
	return render(request,'listings.html',context)