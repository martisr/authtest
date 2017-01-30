from django import forms
from django.contrib.auth.forms import AuthenticationForm

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

    # def __init__(self, *args, **kwargs):
    #    super(StepForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #    raise ValidationError('Not within 3 days')