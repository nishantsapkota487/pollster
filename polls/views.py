from django.shortcuts import render
from polls.models import Question, Choice
# Create your views here.
def index(request):
    return render(request, 'home.html')

def question(request):
     questions = list(Question.objects.all())
     return render(request, 'question.html', {'poll_questions':questions})

def question_option(request, question_id):
    question = Question.objects.get(id=question_id)
    options = list(question.choice_set.all())
    return render(request, 'options.html', {'options':options, 'question':question, 'question_id':question.id})

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    option = question.choice_set.all()
    return render(request, 'results.html', {'options':option})

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    option = question.choice_set.all()
    choice = question.choice_set.get(pk=request.POST["choice"])
    choice.votes += 1
    choice.save()
    return render(request, 'results.html', {'options':option, 'choice':choice})
