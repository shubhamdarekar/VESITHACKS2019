"""myproject1 URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    
    url('^$',views.index,name= 'index'),
    url('^index$',views.index,name= 'Index'),
    url('^Login/$',views.Login,name = 'Login'),
    url('^systemad',views.openadmin),
    url('^empdash/$',views.openemp),
    url('^dept/$',views.opendept),
    url('^reportform/$',views.openrpt),
    url('^loginVerify/$',views.verifyLogin),
    url('^adminDashboard/$',views.adminDash),
    url('^logout/$',views.logout),
    url('^mdDashboard/$',views.mdDash),
    url('^hrDashboard/$',views.hrDash),
    url('^dhDashboard/$',views.dhDash),
    url('^dtDashboard/$',views.dtDash),
    url('^associateDashboard/$',views.associateDash),
    url('^employeeDashboard/$',views.employeeDash),
    url('^adduser/$',views.adduser)

]
