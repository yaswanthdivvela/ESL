from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Acc

def homepage(request):
    return render(request,'accounts/loginPage.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        acc=Acc.objects.filter(username=username)
        if user is not None:
           for a in acc: 
            if a.isgov == True:
              auth.login(request,user)  
              return redirect('govlists')
            else:
              auth.login(request,user)
              return redirect('prevorders')
              
        else:
            u=User.objects.filter(email=username)
            u=u[0].username
            user1=auth.authenticate(username=u,password=password)
            acc1=Acc.objects.filter(username=u)
            if user1 is not None:
             for a in acc1:  
              if a.isgov == True:
                auth.login(request,user1)  
                return redirect('govlists')
              else:
                 auth.login(request,user1)
                 return redirect('prevorders')
                
            else:
               messages.error(request,'Invalid credentials')
               return redirect('login')
    else:
        return render(request,'accounts/loginPage.html')

def signup(request):
    if request.method == 'POST':
        #messages.error(request,'Testing')
        #return redirect('homepage')
        username=request.POST['usernamesignup']
        email=request.POST['emailsignup']
        password=request.POST['passwordsignup']
        password2=request.POST['passwordsignup_confirm']
        fname=request.POST['fname']
        lname=request.POST['lname']
        area=request.POST['area']
        pin=request.POST['pin']
        acc=request.POST['acc']
        ifsc=request.POST['ifsc']
        bname=request.POST['bname']

        #password validation
        if password == password2:
          if User.objects.filter(username=username).exists():
            messages.error(request,'Username exists')
            return redirect('signup')
          else:
            if User.objects.filter(email=email).exists():
                messages.error(request,'email exists')
                return redirect('signup')
            else:
                #good
                user=User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
                user.save()
                acc=Acc(username=username,area=area,pin=pin,acc=acc,ifsc=ifsc,bname=bname,isgov='False')
                acc.save()
                return redirect('login')
        else:
          messages.error(request,'Passwords donot match')
          return redirect('signup')
    else:
        return render(request,'accounts/signup.html')

def logout(request):
   if request.method=='POST':
    auth.logout(request)
    return redirect('index')
