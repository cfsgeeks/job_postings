from django.views.generic import ListView, DetailView
from job_postings.models import Job
import datetime

TODAY = datetime.datetime.today()

class JobList(ListView):
    queryset = Job.objects.filter(closing_date__gte=TODAY)

class JobDetail(DetailView):
    #model = Job
    #queryset = Job.objects.filter(closing_date__gte=TODAY)
    def get_object(self):
        pk_lookup = request.path.split('/')[-1]
        return get_object_or_404(Job, pk=pk_lookup)