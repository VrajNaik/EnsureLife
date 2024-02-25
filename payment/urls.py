from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
path("appoinment",views.appoinment, name = "appoinment"),
path("handlerequest/",views.handlerequest, name = "handlerequest"),
path('accounts/', include('accounts.urls')),
path('Insurance/', include('Insurance.urls')),

    ]