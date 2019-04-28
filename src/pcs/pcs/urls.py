"""pcs URL Configuration

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
from django.views.generic.base import TemplateView
from registration import views as regViews
from checkin import views as checkViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', regViews.register, name='register'),
    path('login/', regViews.login, name='login'),
    path('logout/', regViews.logout, name='logout'),
    path('profile/', regViews.profile, name='profile'),
    path('profile/manage', regViews.manage, name='manage'),
    path('profile/courses', regViews.courses, name='courses'),
    path('profile/options', regViews.options, name='options'),
    path('checkin/', checkViews.swipeCheckin, name='checkin'),
    path('emailcheckin/', checkViews.emailCheckin, name='emailcheckin'),
    path('createcsv/', TemplateView.as_view(
        template_name='createCSV.html'), name='createcsv'),
    path('teamcsv/', regViews.teamcsv, name='teamcsv'),
    path('accountscsv/', regViews.accountscsv, name='accountscsv'),
]
