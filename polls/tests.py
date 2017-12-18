import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice

# Create your tests here.
class QuestionMethodTests(TestCase):

    
    def test_was_published_recently_with_future_question(self):
        """
        was_published recently method should return False for questions
        whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
        self.assertEqual(timezone.now().day, datetime.datetime.now().day)
    
    
    def test_string_representation_of_object_is_returned(self):
        """
        question_text should be returned when Question object is called
        """
        question = Question()
        self.assertEqual(question.__str__(), question.question_text)
    
    
    def test_was_published_recently_with_recent_question(self):
            """
            was_published_recently should return true for whose
            pub_date is within the last days
            """
            time = timezone.now() - datetime.timedelta(hours=1)
            recent_question = Question(pub_date=time)
            self.assertEqual(recent_question.was_published_recently(), True)
            
    def test_Question_attributes_type(self):
            """
            check that methof variables hold proper value
            and value types
            """
            question = Question()
            boolean = question.was_published_recently.boolean
            admin_field = question.was_published_recently.admin_order_field
            short_description = question.was_published_recently.short_description
            self.assertEqual(type(admin_field), str)
            self.assertEqual(admin_field, 'pub_date')
            self.assertEqual(type(boolean), bool)
            self.assertEqual(boolean, not None)
            self.assertEqual(type(short_description), str)
            
        
                
            
# Choice Class
class ChoiceAttributeTests(TestCase):
    
    def test_choice_text_value_type(self):
        is_a_string = str
        choice = Choice()
        self.assertEqual(type(choice.choice_text), is_a_string)
        
    def test_vote_value_type(self):
        is_an_int = int
        choice = Choice()
        choice.question = Question(question_text='how are you', pub_date=timezone.now())
        self.assertEqual(type(choice.votes), is_an_int)
        
        
