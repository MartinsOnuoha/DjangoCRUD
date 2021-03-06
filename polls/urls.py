# mysite/polls/urls.py
# map views to url and function call

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	# ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5
    url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results
    url(r'^results/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/votes/$', views.vote, name='vote'),
]
