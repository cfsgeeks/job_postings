from django.views.generic import ListView
from job_postings.models import Job

class JobList(ListView):
    model = Job