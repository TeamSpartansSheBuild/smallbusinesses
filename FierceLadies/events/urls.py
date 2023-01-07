from django.urls import path, include
from .views import EventDelete
from . import views

urlpatterns = [
    path('events/', views.eventList, name='events'),
    path('event-detail/<int:pk>', views.eventPage, name='event-detail'),
    path('event-create/', views.createEvent, name='event-create'),
    path('event-delete/<int:pk>', EventDelete.as_view(), name='event-delete'),
    path('event-update/<int:pk>', views.updateEvent, name='event-update'),
    path('delete-comment/<int:pk>', views.deleteComment, name = 'delete-comment')
]
