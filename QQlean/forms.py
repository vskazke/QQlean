from django import forms
from .models import *



class ShortForm(forms.ModelForm):
    
    class Meta:
        model = Short
        exclude = ['']

class CallBackForm(forms.ModelForm):
    
    class Meta:
        model = CallBack
        exclude = ['']



