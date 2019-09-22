from django.http import HttpResponse
from django.shortcuts import render
#from django.db import connection
#from .models import EvaluationApp
from django.template import loader
#from django.template import context
#import mysql.connector

def index(request):
	return render(request,"EvaluationApp/index.html")
# Create your views here.

def Login(request):
	return render(request,"EvaluationApp/loginpage.html")