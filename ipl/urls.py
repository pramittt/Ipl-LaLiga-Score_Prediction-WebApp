from django.urls import path
from . import views

urlpatterns =[
    path('',views.ipl,name='ipl'),
    path('home',views.home,name='home'),
    path('predict',views.predict,name='predict')
]

