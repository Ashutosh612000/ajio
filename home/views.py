from django.shortcuts import render
from django.http import HttpResponse
from home.models import Home_Detail


def index(request):
    Hdata = Home_Detail.objects.all()
    
    context = {
        "homedata": Hdata
    }
    return render(request,'home.html',context)

    
# Create your views here.
