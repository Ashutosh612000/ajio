from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product_list

def index(request):
    Pdata  = Product_list.objects.all()
    return render(request,'product.html',{'product_data':Pdata})
# Create your views here.
