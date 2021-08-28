from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password )

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'residency/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def products(request):
    return render(request, 'residency/home.html')

def dashboard(request):
    return render(request, 'residency/dashboard.html')

def resident(request):
    return render(request, 'residency/resident.html')

def report(request):
    return render(request, 'residency/report.html' )




