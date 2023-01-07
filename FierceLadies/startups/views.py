from django.shortcuts import render
# from .forms import startupModelForm
from django.contrib.auth.models import User
from .models import startupModel
from accounts.models import EmployeeOrEmployer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def startupFormView(request):
    context ={}
 
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

    return render(request, "startups/startupForm.html", context)

class startupList(ListView):
    model = startupModel
    context_object_name = 'startups'


class startupDetail(DetailView):
    model = startupModel
    context_object_name = 'startup'

@login_required
def mystartup(request):
    user = request.user
    if user is not None:
        auth_login(request, user)
        employee_or_employer = EmployeeOrEmployer.objects.filter(user=user)
        is_employer = [i.is_employer for i in employee_or_employer]
        print(is_employer)
        if is_employer[0] == True:
            username = user.username
            startups = startupModel.objects.filter(user=user)

            context = {'username':username,'startups':startups}
    else:
        context = {}
    return render(request,'startups/mystartup.html',context)