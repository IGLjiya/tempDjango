from tkinter.font import names

from django.urls import path

from old_app import views

urlpatterns = [
  path('',views.home,name = 'home')
]