from django.urls import path

from newApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('test',views.test,name='test')
]