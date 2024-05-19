from django import forms
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