# /polls/models.py
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



# Create your models here.

# Question Model
@python_2_unicode_compatible # only if you need to support python 2
class Question(models.Model):
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # create method (w_p_r) attributes
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'




    # class variables to represent database field in models
    # Each field is represented by an instance of a Field class
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# Choice Model
@python_2_unicode_compatible # only if you need to support python 2
class Choice(models.Model):

    # should return a string
    def __str__(self):
        return self.choice_text

    # class variables to represent database field in models
    # each choice is related to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
