from django import forms

class ThreadForm(forms.Form):
    content = forms.CharField(label='Comment: ', max_length=100)