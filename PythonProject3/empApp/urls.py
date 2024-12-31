from tkinter.font import names

from django.urls import path

from empApp import views

urlpatterns =[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('addemp',views.addemp,name='addemp'),
    path('viewemp',views.viewemp,name='viewemp'),
    path('delete/<int:id>/',views.deleteData,name='delete'),
    path('update/<int:id>/',views.updateData,name='update')
]