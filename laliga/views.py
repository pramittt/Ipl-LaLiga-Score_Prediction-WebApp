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

        token=['703d8acf-c342-44f4-96aa-80ffb2174533','4d48d621-1fd3-4210-a80f-5de0508a4184',
                'f79e72ae-a0ab-4275-bd68-20413612ee49','bab0c7fb-dae7-41aa-b333-192b59067ee3',
                '667b3d95-12f1-43c9-9f68-fd1ddbdf6c38','fac65d1e-2914-42b5-8107-c0e4e7d68ded',
                'cff9918a-cc73-44c1-aba3-80d32407abe9','4840a424-a23a-41f7-81a3-0ca5e1638c23',
                '52fbf666-ee2c-48ca-80a8-71284a9e6f19','cbf6046b-fc2f-4a78-a042-ce7650529109',
                '1190c779-cc5d-4e59-8317-706536a34879','52cbba22-edaf-436c-9590-4fb6ba411929',
                '2579c39e-8603-463e-962f-300e6807e72e','961cd48d-22ea-4395-bcf3-467fe1f7b77e',
                '0dac7291-70c5-455f-8876-bdba573db77a','ef7ad438-0a7f-4c02-929a-4bdb0e8025dc',
                'b25ec2c9-1953-48d3-8534-d9a98760ce59','d64a7c00-fba3-4496-b42f-6b525a13c15d',
                'c5b9588f-7577-4d4f-863f-1e4e04a69f32','baac8391-aee4-4c1c-a6a1-a8601f1dba7e']

        if(home_team==away_team or home_team=='Home Team Name' or away_team=='Away Team Name' or half_home=='' or half_away==''):
            messages.info(request,'Something went wrong')
            return render(request,'laliga.html')
        
        token_home=token[team.index(home_team)]
        token_away=token[team.index(away_team)]

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
        return render(request,'laliga.html', {'home':home_team,'away':away_team,'home_goal':str(pred1),'away_goal':str(pred2),
                                                'home_token':token_home,'away_token':token_away})
