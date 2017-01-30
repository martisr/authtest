from time import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from django.db.models import Sum


class MyUser(AbstractUser):

    def get_monthly_steps(self):
        # TODO: Filter by current month
        return self.steps.filter().aggregate(Sum('steps'))

    def stepsList(self):
        return Step.objects.order_by('insertion_date')

class Step(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='steps')
    steps = models.IntegerField(max_length=5)
    insertion_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.steps)



