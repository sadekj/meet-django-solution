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
	return render(request, 'polls/detail.html', {'poll' : poll})

def results(request, poll_id):
	p = Poll.objects.get(pk=poll_id)
	return render(request, 'polls/results.html', {'poll' : p})

def vote(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)
	selected_choice = poll.choice_set.get(pk=request.POST['choice'])
	selected_choice.votes += 1
	selected_choice.save()
	return render(request, 'polls/detail.html', {'poll' : poll})
