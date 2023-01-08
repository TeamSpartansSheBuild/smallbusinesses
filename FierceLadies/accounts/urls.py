from django.urls import path
from accounts import views

urlpatterns = [
    path('EmployeeSignup',views.epySignup,name='epySignup'),
    path('EmployerSignup',views.epyrSignup,name='epyrSignup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    
]