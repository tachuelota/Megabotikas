from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,Http404
from .models import Question,Choice
from django.template import  loader

from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('Prueba/index.html')
    context={'latest_question_list':latest_question_list}
    #out_put=', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(out_put)
    return HttpResponse(template.render(context,request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'Prueba/index.html', context)

def detail(request, question_id):
    try:
        question= Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request,'Prueba/detail.html',{'question':question})

def detail(request, question_id):

    question = get_object_or_404(Question,pk=question_id)

    return render(request, 'Prueba/detail.html', {'question': question})


    #return HttpResponse("You're looking at question %s. "% question_id)
def results(request, question_id):
    response="You're looking at results of question %s. "
    return HttpResponse(response% question_id)


def vote(request, question_id):
    question= get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'Prueba/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('Prueba:results',args=(question.id,)))
    #return HttpResponse("You're looking at question %s. "% question_id)


def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return  render(request,'Prueba/results.html',{'question':question})

