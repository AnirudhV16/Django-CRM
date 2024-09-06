from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
# Create your views here.


def home(request,*args,**kwargs):
    #check if person logged in if person logged in then he will
    #see the list of details (only get request)
    #if not then he will provide details using which he logs in
    print(request.POST)
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been loggededd in.")
            return redirect('home')
        else:
            messages.success(request,"there was an error logging in....")
            return redirect(home)
    else:
        return render(request,'home.html',{})

def logout_user(request,*args,**kwargs):
    logout(request)
    messages.success(request,"you have successfully logged out....")
    return redirect('home')
def register_user(request,*args,**kwargs):
    return render(request,"register.html",{})