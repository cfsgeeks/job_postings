from django.conf.urls import url
from job_postings.views import JobList, JobDetail

urlpatterns = [
    url(r'^$', JobList.as_view()),
    url(r'^job/(?P<title>\w)/$', JobDetail.as_view()),
]
