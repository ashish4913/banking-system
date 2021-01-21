from django.shortcuts import render
from .models import Customers,Transfer
from . forms import transferform
# Create your views here.
def home(request):
    return render(request,'home.html')
def list(request):
    customer=Customers.objects.all()
    return render(request,'list.html',{'customers':customer})
def Transfer_money(request,id):
    user=Customers.objects.get(pk=id)
    if request.method=='POST':
        form	=	transferform(request.POST)
        if	form.is_valid():
            cd	=	form.cleaned_data
            u=cd['tx_to']
            amount=cd['amount']
            c=Customers.objects.get(first_name=u)
            if(user.current_balance<amount):
                
                
                return render(request,'transfer.html',{'user':user,'form':transferform,'msg':"INSUFFUCIENT BALANACE"})
            else:
                user.current_balance-=amount
                user.save()
                #print(user.current_balance)
                c.current_balance+=amount
                c.save()
                #print(c.current_balance)
                t=Transfer.objects.create(tx_from=user,tx_to=u,amount=amount)
                t.save()
                return render(request,'transfer.html',{'user':user,'form':transferform,'msg':"Transaction done Sucessfully"})

    return render(request,'transfer.html',{'user':user,'form':transferform})
def history(request):
    h=Transfer.objects.all()

    return render(request,'transaction.html',{'history':h})