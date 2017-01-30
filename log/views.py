from django.core import urlresolvers
from django.db.models import Sum

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import StepForm
# from log.forms import StepForm
# from log.forms import StepForm
# from log.forms import StepForm
from django.template import RequestContext
from django.views import generic

from log.models import Step


@login_required(login_url="login/")
def home(request):
    print (request.user.get_monthly_steps())
    print (request.user.stepsList())
    return render(request, "home.html")


def add_steps(request):
    form = StepForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            #form.save()
            steps = form.save(commit=False)
            steps.user = request.user
            steps.save()

            return HttpResponseRedirect('/')


    return render(request, 'add.html', {'form': form})
