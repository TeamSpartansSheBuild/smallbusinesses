from django.shortcuts import render
# from .forms import startupModelForm
from django.contrib.auth.models import User
from .models import startupModel
from owners.models import owner
from owners.views import onwersFormView
from accounts.models import EmployeeOrEmployer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from events.models import Event

# Create your views here.
def startupFormView(request):

    user =  request.user
    if user is not None:
        auth_login(request, user)
        employee_or_employer = EmployeeOrEmployer.objects.filter(user=user)
        is_employer = [i.is_employer for i in employee_or_employer]
    
    if is_employer == True:
 
        if request.method == 'POST':
            logo = request.POST['logo']
            name = request.POST['name']
            description = request.POST['description']
            founded = request.POST['founded']
            location = request.POST['location']
            website = request.POST['website']

            user = request.user

            startup = startupModel.objects.create(user=user,logo=logo,name=name,description=description,
                                                    founded=founded,location=location,website=website)
            startup.save()

    context={'is_employer':is_employer}

    return render(request, "startups/startupForm.html", context)

class startupList(ListView):
    model = startupModel
    context_object_name = 'startups'


def startupDetail(request,slug):
    startup = startupModel.objects.get(slug=slug)
    owners = owner.objects.filter(startupName=startup)

    user =  request.user
    if user is not None:
        try:
            auth_login(request, user)
            employee_or_employer = EmployeeOrEmployer.objects.filter(user=user)
            is_employer = [i.is_employer for i in employee_or_employer]
            if is_employer:
                context = {'startup':startup,'owners':owners,'is_employer':is_employer[0]}
                return render(request,'startups/startupModel_detail.html',context)
        except:
            pass

    context = {'startup':startup,'owners':owners}
    return render(request,'startups/startupModel_detail.html',context)

@login_required
def mystartup(request):
    user = request.user
    if user is not None:
        auth_login(request, user)
        employee_or_employer = EmployeeOrEmployer.objects.filter(user=user)
        is_employer = [i.is_employer for i in employee_or_employer]

        if is_employer[0] == True:
            username = user.username
            startups = startupModel.objects.filter(user=user)

            context = {'username':username,'startups':startups}
    else:
        context = {}
    return render(request,'startups/mystartup.html',context)


def home(request):
    events = Event.objects.all()
    startups = startupModel.objects.all()
    context = {
        'events' : events,
        'startups': startups,
    }
    return render(request,'home.html',context)