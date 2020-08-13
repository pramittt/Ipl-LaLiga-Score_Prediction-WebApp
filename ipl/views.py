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
        token=['b67caff6-7524-42cb-874e-b5cef45d6088','8a441173-ce0f-42fb-89e3-5e5ccfde4839',
                '670c159a-0c22-448a-b064-90adab97e5cb','34c111f9-3794-42eb-b446-112a96e1e660',
                '50aee1e6-6032-4195-91c2-8d6d72b7b598','41fea1a5-652a-4b1e-9c5d-820770e226be',
                'e414232d-2447-46b5-b1b0-3be72986ed7b','b0ecb2e3-7f61-4a84-baec-1df742d2e702']

        if(bowl_team==bat_team or bat_team=='Batting Team' or bowl_team=='Bowling Team' or overs=='' or runs=='' or 
            wickets=='' or last4=='' or int(last4)>int(runs) or int(wickets)>9 or int(overs)<5 or int(overs)>15):
            messages.info(request,'Something went wrong')
            return render(request,'ipl.html')

        token_bat=token[teams.index(bat_team)]
        token_bowl=token[teams.index(bowl_team)]
        
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
        return render(request,'ipl.html', {'bat_team':bat_team,'bowl_team':bowl_team,'total1':pred1-10,'total2':pred1+15,'bat_token':token_bat,
                                'bowl_token':token_bowl})


