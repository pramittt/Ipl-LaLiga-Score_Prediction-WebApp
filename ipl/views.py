from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import pickle
import numpy as np
# Create your views here.

inn1 = 'ipl/inn1-model-score.pkl'
lasso1 = pickle.load(open(inn1, 'rb'))
inn2 = 'ipl/inn2-model-score.pkl'
lasso2 = pickle.load(open(inn2, 'rb'))

def ipl(request):
    return render(request,'ipl.html')
def home(request):
    return redirect('/')

def predict(request):
    if(request.method=='POST'):
        bat_team=request.POST['BatTeam']
        bowl_team=request.POST['BowlTeam']
        overs=request.POST['Overs']
        runs=request.POST['Runs']
        wickets=request.POST['Wickets']
        last4=request.POST['Runs_4over']
        teams=['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab','Kolkata knight Riders',
                'Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad']
        tmp=[]
        f1=[0.0]*8
        f1[teams.index(bat_team)]=1.0
        tmp+=f1
        f1=[0.0]*8
        f1[teams.index(bowl_team)]=1.0
        tmp+=f1
        tmp+=[float(overs),float(runs),float(last4),float(wickets)]
        data = np.array([tmp])
        pred1 = int(lasso1.predict(data)[0])
        if(pred1<int(runs)):
            pred1=int(runs)+3
        return render(request,'ipl.html', {'bat_team':bat_team,'bowl_team':bowl_team,'total':str(pred1)})


