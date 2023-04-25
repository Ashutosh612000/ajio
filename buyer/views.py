from django.shortcuts import render
from django.http import HttpResponse
from buyer.models import Buyer_Detail

def index(request):
    Bdata = Buyer_Detail.objects.all()
    # Bdata = Buyer_Detail.objects.get(id =id)

    print(Bdata)

    context = {
        'buyerdata': Bdata
    }
    return render(request, 'buyer.html',context)

def buyer(request):
    if request.method == 'POST':
        print("======================================")

        name = request.POST.get('name','')
        phone = request.POST.get('number','')
        email = request.POST.get('email','')
        # print(request.POST.get("name"))
        # print(request.data)
        # name = request.POST['name']
        # phone = request.POST['number']
        # email = request.POST['email']

      


        print(name)
        a = Buyer_Detail(Name = name, Mobile = phone, Email = email)
        a.save()

    return render(request, 'savebuyer.html')