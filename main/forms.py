from django import forms
from .models import User_data

class myForm(forms.Form):
	 data = forms.CharField()


    