from django.shortcuts import render
from job_postings.models import Job
import datetime

TODAY = datetime.date.today()

def index(request):
	jobs_list = Job.objects.filter(status='P',closing_date__gte=TODAY).order_by('-publish_date')
	context = {'jobs':jobs_list}
	return render(request,'listings.html',context)