from tkinter.font import names

from django.urls import path

from todoApp import views

urlpatterns =[
    path('',views.home,name='home'),
    path('todo-view',views.view,name='view'),
    path('addtodo',views.addtodo,name='addtodo')

]