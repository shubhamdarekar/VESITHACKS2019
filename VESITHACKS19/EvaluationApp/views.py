from django.http import HttpResponse
from django.shortcuts import render,redirect
#from django.db import connection
#from .models import EvaluationApp
from django.template import loader
#from django.template import context
#import mysql.connector
from EvaluationApp.forms import LoginForm
# from django.db.models import Q
from django.contrib import messages
from .models import User


def index(request):
	return render(request,"EvaluationApp/landing_page.html")
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


# def authlogin(request):
# 	if request.method =='POST':
# 		details = LoginForm(request.POST)
# 		if (details.is_valid()):
# 			return redirect('EvaluationApp/landing page.html')
# 		users = User.objects.get.all()
# 		for user in users:
# 			if details.user == user.email and details.password == user.password:
# 				if user.role == "admin":
# 					return HttpResponse("<h1>Hii admin</h1>",csrfContext)

		
# 		return HttpResponse("<h1>Failed</h1>",)		
		
def verifyLogin(request):
	try:
		if request.method == 'POST':
			email = request.POST['email']
			pwd = request.POST['password']
			user = User.objects.get(email = email)
			
			if pwd == user.password:
				request.session['logged_in'] = user.id
				if user.role == 'ADMIN':
					return redirect('/adminDashboard/')
				elif user.role == 'MD':
					return redirect('/mdDashboard/')
				elif user.role == 'HR':
					return redirect('/hrDashboard/')
				elif user.role == 'DH':
					return redirect('/dhDashboard/')
				elif user.role == 'DT':
					return redirect('/dtDashboard/')
				elif user.role == 'ASSOCIATE':
					return redirect('/associateDashboard/')
				elif user.role == 'EMPLOYEE':
					return redirect('/employeeDashboard/')
	except:
		return HttpResponse("Error!! Invalid Details")



def logout(request):
	try:
		del request.session['logged_in']
	except KeyError:
		pass
	return render(request,"EvaluationApp/landing_page.html")

def adminDash(request):
	# if request.user.is_authenticated:
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/admin-dashboard.html")
	else:
		return HttpResponse("Error")

def employeeDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/employeedash.html")
	else:
		return HttpResponse("Error")
	

def mdDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/mddashboard.html")
	else:
		return HttpResponse("Error")

def hrDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/supervisordash.html")
	else:
		return HttpResponse("Error")

def dtDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/dept-dashboard.html")
	else:
		return HttpResponse("Error")

def dhDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/departmenthead.html")
	else:
		return HttpResponse("Error")

def associateDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/associatedash.html")
	else:
		return HttpResponse("Error")

# def employeeDash(request):
# 	if(request.session['logged_in']):
# 		return render(request,"EvaluationApp/employeedash.html")
# 	else:
# 		return HttpResponse("Error")

def adduser(request):
	return render(request,"EvaluationApp/adduser.html")

def updateuser(request):
	return render(request,"EvaluationApp/updateUser.html")

def deleteuser(request):
	return render(request,"EvaluationApp/deleteuser.html")
	
def employeeDash(request):
	if(request.session['logged_in']):
		return render(request,"EvaluationApp/employeedash.html")
	else:
		return HttpResponse("Error")
	return render(request,"EvaluationApp/mddashboard.html")
	return render(request,"EvaluationApp/admin-dashboard.html")


def search(request):
	if request.method == 'POST':
		srch = request.POST['srh']

		if srch:
			match = User.objects.filter(email=srch)

			if match:
				return render(request,'EvaluationApp/admin-dashboard.html/',{'srh':match})
			else:
				messages.error(request,'No User Found')
		else:
			return redirect('landing_page/')


def adduser_database(request):
	if request.method == 'POST':
		name = request.POST['name']
		username = request.POST['username']
		id = request.POST['id']
		email = request.POST['email']
		pwd = request.POST['password']
		role = request.POST['role']
		dno = request.POST['dno']

		newuser = User()
		newuser.id = id
		newuser.email = email
		newuser.role = role
		newuser.password = pwd
		newuser.dno = dno
		newuser.save()
		return render(request,'EvaluationApp/admin-dashboard.html/')

def updateuser_database(request):
	if request.method == 'POST':
		id = request.POST['id']
		email = request.POST['email']
		pwd = request.POST['password']
		role = request.POST['role']
		dno = request.POST['dno']

		user = User.objects.get(id = id)
		user.email = email
		user.role = role
		user.password = pwd
		user.dno = dno
		user.save()
		return render(request,'EvaluationApp/admin-dashboard.html/')

def deleteuser_database(request):
	if request.method == 'POST':
		id = request.POST['id']

		user = User.objects.get(id = id)
		user.delete()

		return render(request,'EvaluationApp/admin-dashboard.html/')

def evaluateHR(request):
	return render(request, 'EvaluationApp/evaluateHR.html')

def evaluateOperationsDept(request):
	return render(request, 'EvaluationApp/evaluateOperationsDept.html')

def evaluatePublicRelationsDept(request):
	return render(request, 'EvaluationApp/evaluatePublicRelationsDept.html')

def evaluateTreasuryDept(request):
	return render(request, 'EvaluationApp/evaluateTreasuryDept.html')

def evaluateTechnicalDept(request):
	return render(request, 'EvaluationApp/evaluateTechnicalDept.html')

def evaluateCreativityDept(request):
	return render(request, 'EvaluationApp/evaluateCreativityDept.html')	