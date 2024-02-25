from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    path("login",views.login, name = "login"),
    path("register",views.register, name = "register"),
    path("logout",views.logout, name = "logout"),
    path("profile/",views.profile,name="profile"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    ]