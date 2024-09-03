from django import forms

class LocalidadForm(forms.Form):
    nombre = forms.CharField(max_length=100)