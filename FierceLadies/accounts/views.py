from django.shortcuts import render,redirect
from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from accounts.models import EmployeeOrEmployer

# Create your views here.
def epySignup(request):   # employee signup

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        customer = User.objects.create_user(username,email,password)
        customer.save()

        return redirect('login')

    # events = Event.objects.all()
    context = {'events':'events'}

    return render(request, 'accounts/signup.html', context)


def epyrSignup(request): ## employer sigup

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        customer = User.objects.create_user(username,email,password)
        customer.save()

        is_epyr = EmployeeOrEmployer.objects.create(user=customer,is_employer=True)
        is_epyr.save()

        return redirect('login')

    # events = Event.objects.all()
    context = {'events':'events'}

    return render(request, 'accounts/signup.html', context)


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            username = user.username

            return redirect('/')
        else:
            # messages.error(request, "Bad Credentials")
            return redirect('login')

    # events = Event.objects.all()
    context = {'events':'events'}

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')

def handler404(request,exception):
    return render(request,'404.html')


def authentication(request):
    context = {}
    return render(request,'authentication.html',context)

def signup(request):
    context = {}
    return render(request,'accounts/signup.html',context)