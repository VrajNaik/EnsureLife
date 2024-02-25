from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    path("about",views.about, name = "about"),
    path("faq",views.faq, name = "faq"),
    path('accounts/', include('accounts.urls')),
    path('Insurance/', include('Insurance.urls')),
    ]