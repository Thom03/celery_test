from django.shortcuts import render,  HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from celery.result import AsyncResult
from .tasks import increment

import json

# Create your views here.

def index(request):
    return render(request, 'demo/index.html')

def test_page(request):
    return render(request, 'demo/test.html')

# def quick_test(request):
#     job = add.delay(2, 4)
#     return render(request, 'demo/test.html')    

def start_test(request):
    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.result
        context = {
                'check_status': 1,
                'data': "",
                'state': 'STARTING...',
                'task_id': job_id
		}
        return render(request, 'demo/test.html', context)
    else:
        job = increment.delay(120)
        print ("Celery job ID:  {}.".format(job))
        return HttpResponseRedirect(reverse('demo:start_test') + '?job=' + job.id)    