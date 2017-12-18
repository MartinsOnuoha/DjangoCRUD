# /polls/views.py

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Question, Choice

# Create your views

# index view
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# details view
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

# Vote view
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        # request.POST is a dictionary object that
        # lets you access submitted values/data by key name
        # returns id of selected choice as string
        # Note that Django also provides request.GET
        # for accessing GET data in the same way

    except (KeyError, Choice.DoesNotExist):
        # raise KeyError if choice wasn't provided
        # Redisplay the question voting form with an error message
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message':  "Oops! You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()

# Always return an HttpResponseRedirect after successfully
# dealing with a POST data. This prevents data from being posted twice
# if a user hits the back button
#  HttpResponseRedirect takes a single argument: the URL
# to which the user will be redirected
# the reverse function helps to avoid having to hardcode a URL in the view
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# result views
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
