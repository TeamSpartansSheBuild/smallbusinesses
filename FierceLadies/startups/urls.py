from django.urls import path, include
from startups import views

urlpatterns = [
    path('startupForm',views.startupFormView,name='startupFormView'),
    path('startups',views.startupList.as_view(),name='startupList'),
    path('startup/<slug:slug>',views.startupDetail,name='startupDetail'),
    path('mystartup',views.mystartup,name='mystartup'),
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
]
