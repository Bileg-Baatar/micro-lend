"""MicroLending URL Configuration

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
from Catalog import views

urlpatterns = [
    path('', views.home_view, name= 'home'),
    path('contact', views.contact_view, name= 'contact'),
    path('userlog', views.user_view, name= 'userlog'),
    path('user_app', views.create_account_view, name= 'user_app'),
    path('request', views.request_loan_view, name= 'request'),
    path('managerlog', views.manager_view, name= 'managerlog'),
    path('interest', views.interest_view, name= 'interest'),
    path('manager_app', views.create_manager_view, name= 'manager_app'),
    path('loan', views.loan_view, name= 'loan'),
    path('admin/', admin.site.urls, name= 'admin'),
    
]
