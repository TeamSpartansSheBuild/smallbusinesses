from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from startups.models import startupModel
from owners.models import owner

# Create your views here.
def onwersFormView(request):
    if request. method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        positon = request.POST['position']
        mail = request.POST['mail']
        startupName = request.POST['startupName']

        startupName = startupModel.objects.get(name=startupName)
        print(startupName)
        own = owner.objects.create(startupName=startupName,name=name,about=about,
                                    position=positon,mail=mail)
        own.save()
        
    context = {}
    return render(request,'owners/ownerForm.html',context)

class ownerList(ListView):
    model = owner
    context_object_name = 'owners'


class ownerDetail(DetailView):
    model = owner
    context_object_name = 'owner'