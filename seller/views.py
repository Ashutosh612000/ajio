from django.shortcuts import render
from django.http import HttpResponse
from seller.models import Seller_Detail


def index(request):
    SData = Seller_Detail.objects.all()
    return render(request,'seller.html',{'SData':SData})
# Create your views here.
