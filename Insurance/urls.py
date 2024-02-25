from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    path("Insurance",views.Insurance_info, name = "Insurance"),
    path("policyinfo",views.policyinfo, name = "policyinfo"),
    path('accounts/', include('accounts.urls')),
    ]