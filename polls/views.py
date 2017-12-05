# /polls/views.py

# from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Question

# Create your views

# index
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# detail
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

# results
def results(request, question_id):
	response = "You are viewing the results of question %s."
	return HttpResponse(response % question_id)

# Vote
def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)
