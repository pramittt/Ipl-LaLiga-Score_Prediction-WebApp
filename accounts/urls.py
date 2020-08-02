from django.urls import path
from . import views

urlpatterns =[
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('movie_info',views.movie_info,name='movie_info'),
    path('no_operation',views.no_operation,name='no_operation'),
    path('back',views.back,name='back')
]

