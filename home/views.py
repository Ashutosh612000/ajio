from django.shortcuts import render
from django.http import HttpResponse

from home.forms import UserRagistrations
from home.models import Home_Detail
# from ajio.forms import UserForm


def index(request):
    Udata = UserRagistrations()
    # Hdata = Home_Detail.objects.all()
    
    context = {
        # "homedata": Hdata,
        "forms": Udata,
    }
    return render(request,'home.html',context)

    
# Create your views here.
