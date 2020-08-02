from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import pickle
import numpy as np

home = 'laliga/HomeTeam-Score-Model.pkl'
ridge1 = pickle.load(open(home, 'rb'))
away = 'laliga/AwayTeam-Score-Model.pkl'
ridge2 = pickle.load(open(away, 'rb'))

def laliga(request):
    return render(request,'laliga.html')

def home(request):
    return redirect('/')

def predict(request):
    if(request.method=='POST'):
        home_team=request.POST['HomeTeam']
        away_team=request.POST['AwayTeam']
        half_home=request.POST['HTHG']
        half_away=request.POST['HTAG']
        team=['Alaves', 'Ath Bilbao', 'Ath Madrid','Barcelona', 'Betis','Celta','Eibar', 'Espanol', 'Getafe',
                'Granada','Leganes', 'Levante','Mallorca','Osasuna','Real Madrid', 'Sevilla',
                'Sociedad', 'Valencia', 'Valladolid', 'Villareal']
        tmp=[]
        f1=[0.0]*20
        f1[team.index(home_team)]=1.0
        tmp+=f1
        f1=[0.0]*20
        f1[team.index(away_team)]=1.0
        tmp+=f1
        tmp+=[float(half_home),float(half_away)]
        data = np.array([tmp])
        pred1 = int(ridge1.predict(data)[0])
        pred2=  int(ridge2.predict(data)[0])
        return render(request,'laliga.html', {'home':home_team,'away':away_team,'home_goal':str(pred1),'away_goal':str(pred2)})
