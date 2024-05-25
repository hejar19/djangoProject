from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['day', 'period', 'subject']
        widgets = {
            'day': forms.Select(choices=Timetable.DAYS_OF_WEEK),
            'period': forms.Select(choices=Timetable.PERIODS),
            'subject': forms.Select(choices=Timetable.SUBJECTS),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))