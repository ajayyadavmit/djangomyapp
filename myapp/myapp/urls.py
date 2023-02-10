"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',laptopproduct),
    path('mobile/', include('mobile.urls')),
    path("laptop/",laptoplist),
    path('dynamic/<slug:routevalue>',dynamic),
    path("notype/<ntype>",notype),
]

# abc-def-make-group-here-commmand-there SLUG Type of Values 
# <int: value> <str: valueSTR> <slug:valueSLUGTypes>  
# you can specifiy any type of data here <value> it is dynamic values data here >>> 

