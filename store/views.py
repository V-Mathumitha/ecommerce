from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# views.py


def newindexpage(request):
    products=Product.objects.all()
    return render(request,'newindexpage.html',{'products':products})

def about(request):
    return render(request,'about.html',{})
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You Have Been Logged In..."))
            return redirect('newindexpage')
        else:
            messages.success(request,("There was an error please try again..."))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

     
def logout_user(request):
    logout(request)
    message.success(request,("You have been logeged out..Thanks for shopping"))
    return redirect('newindexpage')
def register_user(request):
    return render(request, 'register.html',{})




