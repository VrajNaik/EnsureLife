from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
path("policycompare",views.policycompare, name = "policycompare"),
path("about/",include('devlopment.urls')),
path("compare",views.compare, name = "compare"),
path("premiumpredict",views.premiumpredict, name = "premiumpredict"),
path('predict/',views.predict,name='predict'),
path('accounts/', include('accounts.urls')),
path('Insurance/', include('Insurance.urls')),
    ]