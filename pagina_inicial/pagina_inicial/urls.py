


from django.urls import path
from app_pagina_inicial import views

urlpatterns = [
   path('',views.index,name='index')
   ]
