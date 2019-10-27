from django.shortcuts import render,redirect
from accounts.models import Acc
from listings.models import Listing

def index(request):
    if request.method=='POST':
     username=request.POST['username']
     invoice=request.POST['invoice']
     ref=request.POST['ref']
     l=Listing.objects.all().filter(invoice=invoice)
     l=l[0]
     print('GOV'+l.invoice+' '+l.username)
     l.ref=ref
     l.status=True
     l.save()
     return redirect('govlists')
    else:
     u=request.user.username
     a=Acc.objects.all().filter(username=u)
     a=a[0]
     l=Listing.objects.all().filter(status=False)
     context={
      'listings': l
     }
     if a.isgov:
      return render(request,'govlists/govt.html',context)
     else:
      return redirect('prevorders')
