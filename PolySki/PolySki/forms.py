from django import forms

class FormName(forms.Form):
    imie = forms.CharField()
    nazwisko = forms.CharField()
    email = forms.EmailField()
    opis = forms.CharField(required=False)
    