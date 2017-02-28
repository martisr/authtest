# coding=utf-8
import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import DateField, DateTimeField, DateInput
from functools import partial
from .models import Step


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['steps', 'insertion_date']
        labels = {
            "steps": "Sammud:",
            "insertion_date": "Kuupäev:"

        }
        widgets = {'insertion_date': DateInput(attrs={'class': 'datepicker', 'data_min': -3, 'data_max': 0})}

    def clean(self):
        cleaned_data = super(StepForm, self).clean()
        cleaned_insertion_date = cleaned_data['insertion_date']
        now = datetime.date.today()
        if cleaned_insertion_date < (now - datetime.timedelta(days=3)):
            raise ValidationError(u'Liiga kaua aega tagasi')
        elif cleaned_insertion_date > now:
            raise ValidationError(u'Tuleviku kuupäeva ei saa määrata')

        return cleaned_data
