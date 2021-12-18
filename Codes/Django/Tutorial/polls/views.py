from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.utils import timezone


def index(request):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse("Hello, wolrd. You're at the polls index")
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.filter(pub_date__lte=timezone.now()).get(
            pk=question_id
        )
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse(f"You're looking at question {question_id}")


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
    # return HttpResponse(f"You're voting on question {question_id}")
