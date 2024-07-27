from django import forms

class PatientForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    symptoms = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter symptoms separated by commas'}))
