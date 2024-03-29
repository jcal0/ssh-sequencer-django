from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render


def index(request):
    return render(request, 'sequencer_app/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)