import user
from itertools import count

from django.contrib.auth.models import User
from django.core import urlresolvers
from django.core.mail import EmailMessage

from django.db.models import Sum, F, Count, Max
from django.views.generic import ListView
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import StepForm
# from log.forms import StepForm
# from log.forms import StepForm
# from log.forms import StepForm
from django.template import RequestContext
from django.views import generic

from log.models import Step, current_month, MyUser
#

@login_required(login_url="login/")
def home(request):
    print (request.user.get_monthly_steps())
    print (request.user.get_avg_steps())
    print (request.user.get_min_steps())
    print (request.user.get_max_steps())
    print (request.user.stepsList())
    return render(request, "home.html")


def add_steps(request):
    form = StepForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            steps = form.save(commit=False)
            steps.user = request.user
            steps.save()
            return HttpResponseRedirect('/')

    return render(request, 'add.html', {'form': form})


def top(request):
    data = MyUser.objects.filter(steps__insertion_date__month=current_month).annotate(Sum('steps__steps')) \
        .order_by('-steps__steps__sum')

    data1 = MyUser.objects.filter(steps__insertion_date__month=current_month).annotate(Max('steps__steps')) \
        .order_by('-steps__steps__max')

    return render(request, 'top.html', {'data': data, 'data1': data1})

