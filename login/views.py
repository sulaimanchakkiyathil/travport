from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def login(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            return redirect('/dashboard/')
        else:
            print("not a valid user")
    return render(request,'login.html')
