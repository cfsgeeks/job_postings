from django.views.generic import ListView, DetailView
from job_postings.models import Job
import datetime

TODAY = datetime.datetime.today()

class JobList(ListView):
    queryset = Job.objects.exclude(closing_date__lte=TODAY,status='P')

class JobDetail(DetailView):
    model = Job
    queryset = Job.objects.exclude(closing_date__lte=TODAY,status='P')
