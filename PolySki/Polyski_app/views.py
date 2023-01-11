
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Polyski_app.models import user, UserManager, event, Tracks
from PolySki import forms
from PolySki.forms import RegistrationForm, ReservationForm, EventForm
from django.contrib.auth import login, authenticate
from django.contrib.admin.widgets import AdminSplitDateTime,AdminDateWidget, AdminTimeWidget
from django.views.generic import ListView, DetailView
import requests, math, datetime
import datetime as dt
from datetime import timedelta
from enum import Enum
class weather(Enum):
    Słonecznie = 1
    Pochmurnie = 2
    Burza = 3
    Deszcz = 4
    Snieznie = 5
    def __str__(self):
        return str(self.name)
def form_name_view(request, *args, **kwargs):
    form = EventForm(request.POST )
    users = user.objects.all()
    if request.method == "POST" and form.is_valid():
        event.name = form.cleaned_data.get('name')
        event.dlugosc = form.cleaned_data.get('dlugosc')
        form.save()
        form = EventForm()
    instruktors1 = event.objects.prefetch_related("instruktor").filter(trwa=False)
    for s in instruktors1:
        for u in users:
            if "<QuerySet [{'username': '" + str(u) + "'}]>" == str(s.instruktor.all().values('username')):
                u.is_free = True
                u.save()
    instruktors = event.objects.prefetch_related("instruktor").filter(trwa=True)
    for s in instruktors:
        for u in users:
            if "<QuerySet [{'username': '"    +str(u)+   "'}]>" == str(s.instruktor.all().values('username')):
                u.is_free = False
                u.save()
    users_list = user.objects.order_by('email')
    context = {'users': users_list,'form':form }
    return render(request,'instruktorzy.html',context)
def home(request):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
    API_KEY = "410eb23de6511ac456553a7d4905d23f"
    CITY = "Karpacz"
    url = BASE_URL + CITY+ "&appid=" + API_KEY
    count_track = Tracks.objects.filter(isopened='Otwarta').count()
    all = Tracks.objects.all().count()
    form = Tracks.objects.filter()
    count = user.objects.all().count()
    users_list = user.objects.order_by('email')
    active = sum(user.is_free == True for user in users_list )
    response = requests.get(url).json()
    temp = response['main']['temp']-273.15
    wind = response['wind']['speed'] * 3.6
    id = response['weather'][0]['id']
    if id ==800:
            pogoda = weather(1)
    elif id <=804 and id >= 801 :
            pogoda = weather(2)
    elif id <=232 and id >= 200 and id <=731 and id >= 700:
            pogoda = weather(3)
    elif id <=531 and id >= 500 :
            pogoda = weather(4)
    elif id <=622 and id >= 600 :
            pogoda = weather(5)
    temp = round(temp,1)
    wind = round(wind, 1)
    context = {'count':count, 'temp' : temp,'pogoda': pogoda,'wind':wind,'edit_form':form,'nowactive':active, 'all':all, 'count_track':count_track}
    return render(request,'home.html',context)
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"Jesteś juz zalogowany jako {user.email}.")
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email = email, password = raw_password)
            login(request, user)
            HttpResponse(f"Udało sie zarejestrowac")
            return redirect('login')
    return render(request,'registration/register.html',context)
def events(request, *args, **kwargs):
    events_list = event.objects.order_by('-data')
    users_list = user.objects.order_by('email')
    form = EventForm(request.POST )
    if request.method == "POST" and form.is_valid():
        event.name = form.cleaned_data.get('name')
        event.dlugosc = form.cleaned_data.get('dlugosc')
        form.save()
        form = EventForm()
    context = {'events': events_list,'users':users_list,'form':form}
    return render(request,'events.html',context)

def blue_track(request, name=Tracks.name):
    form = Tracks.objects.filter(name=name)
    args={'edit_form':form, 'name':name, 'closed':'Zamknięta', 'opened':'Otwarta'}
    return render(request,'blue_track.html',args)

def tracks(request,name=Tracks.name):
    count = Tracks.objects.filter(isopened='Otwarta').count()
    form = Tracks.objects.filter()
    args={'edit_form':form, 'name':name, 'closed':'Zamknięta', 'opened':'Otwarta', 'count':count}
    return render(request,'track.html',args)
