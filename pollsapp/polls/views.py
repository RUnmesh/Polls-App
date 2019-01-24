# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import question , choice
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import QuesForm , ChoiceForm
from django.utils import timezone

def test(request) :
    questions = question.objects.order_by('-pub_date')
    context = {'questions' : questions}
    return render( request , 'polls/index.html' , context)

def details(request , ques_id) :
    ques = get_object_or_404(question , pk = ques_id )
    context = {
        'question' : ques
    }
    return render( request , 'polls/details.html' , context)

def results (request , ques_id) :
    ques = get_object_or_404(question , pk = ques_id )
    choices = ques.choice_set.order_by('-votes')
    sum = 0
    for i in choices :
        sum += i.votes
    context = {
        'question' : ques,
        'sum' : sum,
        'choices' : choices
    }
    return render( request , 'polls/results.html' , context)

def votes (request , ques_id) :
    ques = get_object_or_404(question , pk = ques_id)
    selected_choice_id = request.POST['choice']
    selected_choice = ques.choice_set.get(pk = selected_choice_id)
    selected_choice.votes += 1 
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results' , args = (ques.id,)))

def add (request) :
    
    if request.method == 'POST' :
        form = QuesForm(request.POST)
        if form.is_valid() :
            ques = form.save(commit = False)
            ques.pub_date = timezone.now()
            ques.save()
            return redirect('polls:test')
    
    else :
        form = QuesForm()
        return render( request , 'polls/add.html' , {'form' : form})

def choiceadd (request , ques_id) :
    
    if request.method == 'POST' :
        form = ChoiceForm(request.POST)
        if form.is_valid() :
            choice = form.save(commit = False)
            choice.votes = 0
            choice.question = question.objects.get(pk = ques_id )
            choice.save()
            return redirect('polls:details' , ques_id = choice.question.id)
    
    else :
        form = ChoiceForm()
        return render( request , 'polls/add_choice.html' , {'form' : form})