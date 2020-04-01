from polls.views import index, question,question_option, results,vote
from django.urls import path

app_name = 'polls'

urlpatterns = [
    path('', index, name = 'index'),
    path('questions/',question, name = 'question' ),
    path('question/<int:question_id>', question_option, name = 'question_option'),
    path('question/results/<int:question_id>',results, name = 'vote'),
    path('question/vote/<int:question_id>', vote, name = 'results')

]
