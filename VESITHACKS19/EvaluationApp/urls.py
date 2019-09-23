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
    url('^adduserdatabase/$',views.adduser_database),
    url('^updateuserdatabase/$',views.updateuser_database),
    url('^deleteuserdatabase/$',views.deleteuser_database),
    url('^adminDashboard/$',views.adminDash),
    url('^logout/$',views.logout),
    # url('^mdDashboard/$',views.mdDash),
    url('^mdDashboard/$',views.mdDash),
    url('^hrDashboard/$',views.hrDash),
    url('^dhDashboard/$',views.dhDash),
    url('^dtDashboard/$',views.dtDash),
    url('^associateDashboard/$',views.associateDash),
    url('^employeeDashboard/$',views.employeeDash),
    url('^adduser/$',views.adduser),

# md daashboard functionality
    url('^evaluateHR/$',views.evaluateHR),
    url('^evaluateOperationsDept/$',views.evaluateOperationsDept),
    url('^evaluatePublicRelationsDept/$',views.evaluatePublicRelationsDept),
    url('^evaluateTreasuryDept/$',views.evaluateTreasuryDept),
    url('^evaluateTechnicalDept/$',views.evaluateTechnicalDept),
    url('^evaluateCreativityDept/$',views.evaluateCreativityDept),

# hr dashboard functionality
    url('^reportform/$',views.reportform),
    url('^assessDepthead/$',views.assessDepthead),
    # url('^assessDeptteam/$',views.assessDeptteam),
    # url('^assessEmployees/$',views.assessEmployees),
    # url('^assessAssociates/$',views.assessAssociates),

    url('^updateuser/$',views.updateuser),
    url('^deleteuser/$',views.deleteuser),
    # url('^hrDashboard/$',views.hrDash),
    # url('^dhDashboard/$',views.dhDash),
    # url('^dtDashboard/$',views.dtDash),
    # url('^associateDashboard/$',views.associateDash),
    # url('^employeeDashboard/$',views.employeeDash),
    url('^search/$',views.search),

]
