from django.urls import path

from . import views

urlpatterns=[
 path('',views.index,name='prevorders'),
 path('new',views.neworder,name='neworder')
]
