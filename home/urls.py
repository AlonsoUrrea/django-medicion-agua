from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),

  path('tanques/', views.tanques, name='tanques'),
  path('tanques/<int:id_tanque>', views.tanque, name="tanque"),
]
