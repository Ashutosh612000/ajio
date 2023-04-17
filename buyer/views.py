from django.shortcuts import render
from django.http import HttpResponse
from buyer.models import Buyer_Detail

def index(request):
    Bdata = Buyer_Detail.objects.all()

    context = {
        'buyerdata': Bdata
    }
    return render(request, 'buyer.html',context)

# Create your views here.
