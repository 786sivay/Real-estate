from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        if password==password2:
            print('shi hai')
            if User.objects.filter(username=username).exists():
                messages.error(request,'user already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already taken')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email,password=password,first_name=firstname,last_name=lastname)
                    messages.success(request,'You are registered')
                    return redirect('login')
                
            
            
        else:
            messages.error(request,"PASSWORD DOESNOT MATCH")
            print('shi ni hai')
            return redirect('register')
    else:
        
        return render(request,"accounts/register.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print('sone')
            auth.login(request,user)
            messages.success(request,'You are successfully logged in ')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    return render(request,"accounts/login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You are logged out")
        return redirect('index')

def dashboard(request):
    

    return render(request,"accounts/dash.html")
