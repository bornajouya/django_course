from django import forms

class bookForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your name', max_length=100)
    message = forms.CharField(label='Your name', max_length=100)
