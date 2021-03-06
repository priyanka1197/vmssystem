"""visitor_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_login/', views.loginPage, name = 'admin_login'),
    path('manager_login/', views.manager_login, name = 'manager_login'),
    path('manager_login/managerguest/', views.managerguest, name = 'managerguest'),
path('manager_login/managerguest/guestinfo/', views.guestinfo, name='guestinfo'),
    path('dashboard/', include('accounts.urls'), name = 'doctors'),
    path('doctors/', views.doctors, name = 'doctors'),
    path('doctors/guest/',views.guestdetail, name='guest'),
    path('save_guest/', views.save_guest, name='save_guest'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkin_submit/', views.checkinsubmit, name='checkinsubmit'),
    path('company/', views.company, name='company')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
