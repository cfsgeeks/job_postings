from django.views.generic import ListView
from job_postings.model import Job

class JobList(ListView):
    model = Job