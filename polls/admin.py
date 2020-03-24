from django.contrib import admin
from .models import Question, Choice
class ChoiceInline(admin.StackedInline):
        model=Choice
        extra = 3

class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	fieldsets = [(None, {'fields':['question_text']}),
                     ('Data information',{'fields':['pub_date'],'classes':['collapse']}),
                     ]
	inlines=[ChoiceInline]
		

admin.site.register(Question,QuestionAdmin)
