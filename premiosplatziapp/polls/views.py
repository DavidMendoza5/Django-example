from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Las vistas siempre reciben un parámetro request, el cuál tiene la información que se envía desde la vista
def index(request):
  latest_question_list = Question.objects.all()
  return render(request, "polls/index.html", {
    "latest_question_list": latest_question_list
    })


def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {
    "question": question
  })


def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/results.html", {
    "question": question
  })


def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  # Al ser un formulario el que se manda en el action, se obtiene un POST dentro de request
  print(request.POST)
  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    return render(request, "polls/detail.html", {
      "question": question,
      "error_message": "No elegiste una respuesta"
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))