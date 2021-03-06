from django import forms
from . import models

class Email(forms.Form):
    name = forms.CharField()
    tel = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.EmailUs
        fields = ['name','tel','email','text']