from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets as adminWidget
from django.contrib.admin.widgets import AdminSplitDateTime,AdminDateWidget, AdminTimeWidget

from django.contrib.auth import authenticate
from Polyski_app.models import user,event
CHOICES = (
    (True, "Tak"),
    (False, "Nie")
)
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
class ReservationForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('wolny',)
    wolny = forms.ChoiceField(required=None, choices = CHOICES,label="Jesteś dostępny?" )

class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ('name','dlugosc','instruktor','data')
        widgets = {
            'data': forms.widgets.DateTimeInput(
                attrs={'type': 'datetime-local'})
        }
    name = forms.CharField(label= "Nazwa wydarzenia",required=False)
    dlugosc = forms.IntegerField(label=" Czas trwania",required=False)
    instruktor = forms.ModelMultipleChoiceField(
        queryset=user.objects.all(),
        required=False
    )

