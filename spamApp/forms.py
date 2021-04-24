from django import forms

from .models import Spam

class Spammodel(forms.ModelForm):
    class Meta:
        model = Spam
        fields = [
            'email',
            'title',
            'tresc',
            'time'
        ]





