from django.http import HttpResponse
from django.shortcuts import render
#from django.db import connection
#from .models import EvaluationApp
from django.template import loader
#from django.template import context
#import mysql.connector
from EvaluationApp.forms import LoginForm
from .models import User

def index(request):
	return render(request,"EvaluationApp/landing page.html")
# Create your views here.

def Login(request):
	return render(request,"EvaluationApp/loginpage.html")

def openadmin(request):
	return render(request,"EvaluationApp/admin-dashboard.html")

def openemp(request):
	return render(request,"EvaluationApp/employeedash.html")

def opendept(request):
	return render(request,"EvaluationApp/dept-dashboard.html")

def openrpt(request):
	return render(request,"EvaluationApp/reportform.html")

def authlogin(request):
	if request.method =='POST':
		details = LoginForm(request.POST)
		if (details.is_valid()):
			return redirect('EvaluationApp/landing page.html')
		users = User.objects.get.all()
		for user in users:
			if details.user == user.email and details.password == user.password:
				if user.role == "admin":
					return HttpResponse("<h1>Hii admin</h1>",csrfContext)

		
		return HttpResponse("<h1>Failed</h1>",)		
		

