from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from .forms import SignUpForm,AddRecordform
from .models import Record
# Create your views here.


def home(request,*args,**kwargs):

    records=Record.objects.all()

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
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

def logout_user(request,*args,**kwargs):
    logout(request)
    messages.success(request,"you have successfully logged out....")
    return redirect('home')
def register_user(request,*args,**kwargs):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"you have successfully registered")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,"register.html",{'form':form})
    
    return render(request,"register.html",{'form':form})
def customer_record(request,id):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=id)
        return render(request,"record.html",{"customer_record":customer_record})
    else:
        messages.success(request,"You must be logged in to view that page....")
        return redirect('home')
def delete_record(request,id):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=id)
        delete_it.delete()
        messages.success(request,"record deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"you must be logged in to do that")
        return redirect('home')
def add_record(request):
    form=AddRecordform(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Record Added....")
                return redirect('home')
        return render(request,"add_record.html",{'form':form})
    else:
        messages.success(request,"Must be logged in....")
        return redirect('home')
def update_record(request,id):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=id)
        form=AddRecordform(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been Updated....")
            return redirect('home')
        return render(request,"update_record.html",{'form':form})
    else:
        messages.success(request,"Must be logged in....")
        return redirect('home')



