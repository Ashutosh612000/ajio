from django.shortcuts import render,redirect
from django.http import HttpResponse 
from product.models import Product_list,Grocery,Electronics,Mobile

def index(request):
    P_L_data  = Product_list.objects.all()
    G_data  = Grocery.objects.all()
    E_data = Electronics.objects.all()
    M_data = Mobile.objects.all()


    context = {
        'product_data': P_L_data,
        'grocery_data': G_data,
        'electronics_data': E_data,
        'mobile_data': M_data,

    }
    return render(request,'product.html',context)

#this function for delete product
def delete_data(request,id):
    pi= Grocery.objects.get(id=id)
    pi.delete()
    return redirect('product') 


#this function for update data
def update_data(request,id):
    return render(request,'updatedata.html',{'id':id})



# Create your views here.
