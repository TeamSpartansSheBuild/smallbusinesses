from django.urls import path, include
from startups import views

urlpatterns = [
    path('startupForm',views.startupFormView,name='startupFormView'),
    path('startups',views.startupList.as_view(),name='startupList'),
    path('startup/<int:pk>',views.startupDetail.as_view(),name='startupDetail'),
    path('mystartup',views.mystartup,name='mystartup'),
    path('',views.home,name='home'),
    
]
