from __future__ import absolute_import
import requests
from django.http import Http404
from django.shortcuts import render

from dimagi.pages.models.careers import JobPost
from dimagi.utils.decorators import no_index


def _get_job_post(job_id):
    api_url = "https://api.greenhouse.io/v1/boards/dimagi/jobs/{}".format(job_id)
    data = requests.get(api_url)
    data = data.json()
    if data.get('id'):
        return JobPost(data)


@no_index
def home(request):
    return render(request, 'pages/careers.html')


@no_index
def view_job(request, job_id):
    job = _get_job_post(job_id)
    if not job:
        raise Http404()
    context = {
        'job': job,
    }
    return render(request, 'pages/job.html', context)
