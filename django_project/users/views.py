from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def registercust(request):
    if request.method=="POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var= form.save(commit=False)
            var.is_customer=True
            var.save()
            messages.info(request),"Account registerd, login"
            return redirect('login')
        else:
            messages.warning(request,'Error, Kindly retry')
            return redirect ("registercust")
    else:
        form= RegisterCustomerForm()
        context={'form':form}
        return render(request,'users/registercust.html', context)



def login (request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request,'Successfully Loged in')
            return redirect ("dashboard")
        else :
            messages.warning (request,'Error, Kindly retry')
            return redirect ("login")
    else :
        return render(request,"users/login.html")


def logout (request):
    logout(request)
    messages.info(request,'Logged out')
    return redirect ("login")