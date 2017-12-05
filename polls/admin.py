from django.contrib import admin
from .models import Question, Choice # import models from local dir

class ChoiceInline(admin.TabularInline):
    """ .TabularInline allows choices to be arranged in
    	tabular form in the add question page
    """
    model = Choice
    extra = 2 # By default, provide 3 slots for related choices

#  create a model admin object,
# then pass it as the second argument to admin.site.register()
class QuestionAdmin(admin.ModelAdmin):
    """
     change the order of admin form presentation.
     Categorize form functions
    """
    # The first element of each tuple in fieldsets
    # is the title of the fieldset.
    fieldsets = [

        	('Question', {'fields': ['question_text']}),
         	('Publish Information', {'fields': ['pub_date'], 'classes': ['collapse']}),


	    ]
    # Add Choice as an inline object of QuestionAdmin class
    inlines = [ChoiceInline]

    #  list_display admin option,
    # which is a tuple of field names to display,
    # as columns, on the "change list page" for the object
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # adds a filter sidebar that allows filtering by pub_date
    list_filter = ['pub_date']

    # adds a search box at the top of the change list
    search_fields = ['question_text']

    # include a date-based drilldown navigation by that field
    date_hierarchy = 'pub_date'

# Register your models here.
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

