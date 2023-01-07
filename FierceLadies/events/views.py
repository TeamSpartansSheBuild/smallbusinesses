from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import EventForm
from django.contrib.auth.decorators import login_required

from .models import Event, Comment
# Create your views here.


def eventPage(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        comment_message = request.POST.get('comment-message')
        comment = Comment(user=request.user, event=event,
                          message=comment_message)
        comment.save()
        return redirect('event-detail', pk)
    comments = Comment.objects.filter(event=event)
    context = {
        'event': event,
        'comments': comments,
        'user' : request.user,
    }
    return render(request, 'events/event_detail.html', context)

@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    event = comment.event
    if comment.user != request.user:
        return render(request, 'unauthorized_access.html')
    if request.method == 'POST':
        comment.delete()
        return redirect('event-detail', event.id)
    else:
        context = {
            'comment': comment,
            'event': event,
        }
        return render(request, 'events/comment_delete_confirmation.html', context)

def eventList(request):
    search_area = request.GET.get('search-area')
    if search_area is None:
        search_area = ''
    events = Event.objects.filter(Q(name__icontains=search_area) | Q(
        description__icontains=search_area) | Q(location__icontains=search_area))
    context = {
        'events': events,
        'search_area' : search_area,
    }
    return render(request, 'events/event_list.html', context)

@login_required(login_url='login')
def createEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        event = form.save()
        event.host = request.user
        event.save()
        return redirect('event-detail', event.id)
    else:
        form = EventForm()
        context = {
            'form': form,
        }
        return render(request, 'events/event_form.html', context)

@login_required(login_url='login')
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    if event.host != request.user:
        return render(request, 'unauthorized_access.html')
    if event.host != request.user:
        return redirect('event-detail', event.id)
    elif request.method == 'POST':
        form = EventForm(request.POST)
        event = form.save()
        event.save()
        return redirect('event-detail', event.id)
    else:
        form = EventForm(instance=event)
        context = {
            'event': event,
            'form': form,
        }
        return render(request, 'events/event_form.html', context)



class EventDelete(DeleteView):
    model = Event
    fields = '__all__'
    context_object_name = 'event'
    success_url = reverse_lazy('events')
