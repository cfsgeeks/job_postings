from django.conf.urls import url
from job_postings.views import JobList, JobDetail

urlpatterns = [
    url(r'^job/\w+$', JobDetail.as_view()),
    url(r'^$', JobList.as_view()),]
