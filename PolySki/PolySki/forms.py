from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Polyski_app.models import user
class FormName(forms.Form):
    imie = forms.CharField()
    nazwisko = forms.CharField()
    email = forms.EmailField()
    opis = forms.CharField(required=False)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Podaj adres email')

    class Meta:
        model = user
        fields = ('email', 'username', 'password1', 'password2')
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = user.objects.get(email=email)
        except Exception as e:
            return email
            raise forms.ValidationError(f"Email {email} jest już użyty")
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = user.objects.get(username=username)
        except Exception as e:
            return username
            raise forms.ValidationError(f"Nazwa użytkownika {username} jest już użyta")

