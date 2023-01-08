from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from startups.models import startupModel
from owners.models import owner
from django.contrib.auth import login as auth_login,logout as auth_logout
from accounts.models import EmployeeOrEmployer

# Create your views here.
def onwersFormView(request,slug):
    startupName = slug

    user =  request.user
    if user is not None:
        auth_login(request, user)
        employee_or_employer = EmployeeOrEmployer.objects.filter(user=user)
        is_employer = [i.is_employer for i in employee_or_employer]
    
    if is_employer == True:
        if request. method == 'POST':
            name = request.POST['name']
            about = request.POST['about']
            positon = request.POST['position']
            mail = request.POST['mail']
            # startupName = request.POST['startupName']

            startupName = startupModel.objects.get(slug=slug)
            print(startupName)
            own = owner.objects.create(startupName=startupName,name=name,about=about,
                                        position=positon,mail=mail)
            own.save()

    context = {'startupName':startupName,'is_employer':is_employer}
    return render(request,'owners/ownerForm.html',context)


class ownerList(ListView):
    model = owner
    context_object_name = 'owners'

class ownerDetail(DetailView):
    model = owner
    context_object_name = 'owner'