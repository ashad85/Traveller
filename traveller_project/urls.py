"""
URL configuration for traveller_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from traveller_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('log', log_In, name='log_In'),
    path('regist', regist, name='regist'),
    path('trip', trip, name='trip'),
    path('trip_detail', trip_detail, name='trip_detail'),
    path('delete-data/<int:id>/', delete_data, name='delete_data'),
    path('paym/<int:id>/', paym, name='paym'),
    path('offer_1', offer_1, name='offer_1'),
    path('offer_2', offer_2, name='offer_2'),
    path('offer_3', offer_3, name='offer_3'),
    path('offer_4', offer_4, name='offer_4'),
    path('pro', profile, name='profile'),
    path('lgout', lgout, name='lgout')
]
