from django.shortcuts import render,redirect
from accounts.models import Acc
from listings.models import Listing
from django.contrib import messages

def index(request):
    u=request.user.username
    a=Acc.objects.all().filter(username=u)
    a=a[0]
    l=Listing.objects.all().filter(username=u)
    context={
     'listings': l
    }
    if a.isgov:
     return redirect('govlists')
    else:
     return render(request,'listings/historfarmer.html',context)

def neworder(request):
    if request.method== 'POST':
        username=request.POST['username']
        item=request.POST['item']
        quant=request.POST['quant']
        invoice=request.POST['invoice']
        pic=request.POST['pic']
        if Listing.objects.all().filter(invoice=invoice).exists():
            if Listing.objects.all().filter(invoice=invoice,username=username).exists():
             messages.error(request,'Invoice No. already exists, check in Previours orders')
             return redirect('neworder')
            else:
             messages.error(request,'Duplicate Invoice No.')
             return redirect('neworder')                
        else:
            a=Acc.objects.all().filter(username=username)
            a=a[0]
            l=Listing(accs=a,username=username,item=item,quantity=quant,invoice=invoice,pic=pic)
            l.save()
            return redirect('prevorders')
    else:
     u=request.user.username
     a=Acc.objects.all().filter(username=u)
     a=a[0]
     if a.isgov:
      return redirect('govlists')
     else:
      return render(request,'listings/newfarm.html')
