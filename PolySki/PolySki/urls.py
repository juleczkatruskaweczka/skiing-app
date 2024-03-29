"""PolySki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Polyski_app.views import form_name_view,home, register_view,events,blue_track,tracks
from django.contrib.auth import views as auth_views
from Polyski_app.models import Tracks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('help/',form_name_view),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/',register_view, name='register'),
    path('home/',home),
    path('events/',events),
    path('tracks/', tracks),
    path('track/<str:name>/', blue_track, name='name'),
]