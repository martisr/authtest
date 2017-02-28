from distutils.log import Log
from time import timezone
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models import Sum, Avg, Min, Max
from datetime import datetime, timedelta
from django_cron import CronJobBase, Schedule
from django.template.context_processors import request

current_month = datetime.now().month


class MyUser(AbstractUser):

    def get_monthly_steps(self):
        return self.steps.filter(insertion_date__month=current_month).aggregate(Sum('steps')).values()[0]


    def get_avg_steps(self):
        return self.steps.filter(insertion_date__month=current_month).aggregate(Avg('steps')).values()[0]

    def get_min_steps(self):
        return self.steps.filter(insertion_date__month=current_month).aggregate(Min('steps')).values()[0]

    def get_max_steps(self):
        return self.steps.filter(insertion_date__month=current_month).aggregate(Max('steps')).values()[0]

    def stepsList(self):
        return self.steps.filter(insertion_date__month=current_month)


class Step(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='steps')
    steps = models.IntegerField()
    insertion_date = models.DateField(default=datetime.now()+timedelta(days=-3))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.steps)
