from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Choice
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request
def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list' : latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)
	return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
	return HttpResponse("You are looking at the results of poll "+poll_id)

def vote(request, poll_id):
	return HttpResponse("You are voting on poll "+poll_id)
