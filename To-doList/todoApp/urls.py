from tkinter.font import names

from django.urls import path

from todoApp import views

urlpatterns =[
    path('',views.home,name='home'),
    path("Home",views.home,name='home'),
    path('todoview',views.todoView,name='todoview'),
    # path('todoinput',views.todoinput,name='todoinput'),
    path("todoadd",views.addTodo,name='addTodo'),
    path("404_error",views.error,name='404_error'),

    #delete
    path('delete/<int:id>/',views.deleteData,name="delete"),
    #update
    path('updata/<int:id>/',views.updateData,name='update')
]