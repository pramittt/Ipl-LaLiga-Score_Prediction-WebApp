from django.shortcuts import render
from .models import Team
# Create your views here.
def index(request):
    teams= Team.objects.all()
    return render(request,'index.html',{'teams':teams})