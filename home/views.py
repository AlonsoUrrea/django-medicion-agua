import datetime

from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *

def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/chart-morris.html", context)

def tanques(request):
  tanques = Tanque.objects.all()

  context = { "tanques": tanques }

  return render(request, 'pages/tanques/lista.html', context)
#end def

def tanque(request, id_tanque):
  tanque = Tanque.objects.get(id_tanque=id_tanque)
  mediciones = Medicion.objects\
    .filter(id_sensor=tanque.id_sensor)#\
    #.filter(hora_fecha__gte=datetime.date(2024,7,12))
  nivel = mediciones.last()

  context = { 
    "tanque": tanque,
    "mediciones": mediciones,
    "nivel_actual": nivel
  }

  return render(request, 'pages/tanques/tanque.html', context)
#end def