from django.urls import path
from owners import views

urlpatterns = [
    path('ownerForm/<slug:slug>',views.onwersFormView,name='owner-form'),
    path('owners',views.ownerList.as_view(),name='ownerList'),
    path('owner/<slug:slug>',views.ownerDetail.as_view(),name='ownerDetail'),
]