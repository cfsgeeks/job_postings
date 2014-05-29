from django.conf.urls import url
from job_postings.views import JobList

urlpatterns = [
    url(r'^$', JobList.as_view()),
]
