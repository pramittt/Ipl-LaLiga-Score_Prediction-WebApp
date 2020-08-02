from django.urls import path
from . import views

urlpatterns =[
    path('',views.laliga,name='laliga'),
    path('predict',views.predict,name='predict'),
    path('home',views.home,name='home')
]

