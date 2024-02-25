"""Insurance_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from payment import views as abc
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',include('EnsureLife.urls')),
    #path('',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('devlopment/', include('devlopment.urls')),
    path('Insurance/', include('Insurance.urls')),
    path('policy/', include('policy.urls')),
    path('payment/', include('payment.urls')),
    path('payment/handlerequest/',abc.handlerequest),
    path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)