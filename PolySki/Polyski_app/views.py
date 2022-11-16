
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from Polyski_app.models import Topic, Webpage, AccessRecord, User
from PolySki import forms
def witam(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {'insert_me':"Hello I am from views.py"}
    return render(request,'index.html',context=date_dict)
def help(request):
    my_dict = {'insert_me':"HELPING"}
    return render(request,'help.html',context=my_dict)
def users(request):
    users_list = User.objects.order_by('imie')
    users_dict ={'users':users_list}
    return render(request,'users.html',context=users_dict)
def form_name_view(request):
    users_list = User.objects.order_by('imie')
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            user = User.objects.get_or_create(
                imie=form.cleaned_data['imie'],
                nazwisko=form.cleaned_data['nazwisko'],
                email=form.cleaned_data['email'],
                opis=form.cleaned_data['opis']
            )
        form=forms.FormName()

    context = {'form': form, 'users': users_list}
    return render(request,'users.html',context)

