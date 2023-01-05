
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Polyski_app.models import user, UserManager, Tracks
from django.forms import forms
from PolySki import forms
from PolySki.forms import RegistrationForm
from django.contrib.auth import login, authenticate

def help(request):
    my_dict = {'insert_me':"HELPING"}
    return render(request,'help.html',context=my_dict)
def users(request):
    users_list = user.objects.order_by('imie')
    users_dict ={'users':users_list}
    return render(request,'users.html',context=users_dict)
def form_name_view(request):
    users_list = user.objects.order_by('email')
    context = {'users': users_list}
    return render(request,'users.html',context)

def home(request):
    count = user.objects.all().count()
    form = Tracks.objects.filter()
    context = {'count':count, 'edit_form':form}
    return render(request,'home.html',context)

def blue_track(request, name=Tracks.name):
    form = Tracks.objects.filter(name=name)
    args={'edit_form':form, 'name':name, 'closed':'Zamknięta', 'opened':'Otwarta'}
    return render(request,'blue_track.html',args)

def tracks(request,name=Tracks.name):
    count = Tracks.objects.filter(isopened='Otwarta').count()
    form = Tracks.objects.filter()
    args={'edit_form':form, 'name':name, 'closed':'Zamknięta', 'opened':'Otwarta', 'count':count}
    return render(request,'track.html',args)

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
