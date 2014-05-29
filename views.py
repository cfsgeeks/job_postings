from django.views.generic import ListView
from job_postings.models import Job
import datetime

TODAY = datetime.datetime.today()

class JobList(ListView):
    queryset = Job.objects.filter(closing_date__gte=TODAY)