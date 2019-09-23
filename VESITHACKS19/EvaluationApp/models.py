from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=40,null = True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    d_no = models.ForeignKey('Dept',on_delete = models.SET_NULL,null = True,related_name='%(class)s_requests_created')
    role = models.CharField(max_length = 15)
    password = models.CharField(max_length=20)

class Dept(models.Model):
    dname = models.CharField(max_length = 20)
    dHeadId = models.ForeignKey('User',on_delete = models.SET_NULL,null = True,related_name='%(class)s_requests_created')
    c1 = models.SmallIntegerField()
    c2 = models.SmallIntegerField()
    c3 = models.SmallIntegerField()
    def get_avg(self):
        return (self.c1+self.c2+self.c3)/3
    date = models.DateTimeField(auto_now =True)

class Evaluates(models.Model):
    evaluated_by = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created1')
    evaluation_of = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created')
    e1 = models.SmallIntegerField()
    e2 = models.SmallIntegerField()
    e3 = models.SmallIntegerField()
    e4 = models.SmallIntegerField()
    e5 = models.SmallIntegerField()
    e6 = models.SmallIntegerField()
    e7 = models.SmallIntegerField()
    e8 = models.SmallIntegerField()
    e9 = models.SmallIntegerField()
    e10 = models.SmallIntegerField()
    def get_avg(self):
        return (self.e1+self.e2+self.e3+self.e4+self.e5+self.e6+self.e7+self.e8+self.e9+self.e10)/10
    suggestion = models.TextField()

class HRassessment(models.Model):
    assessedby = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created1')
    assessedof = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created')
    hra1 = models.SmallIntegerField()
    hra2 = models.SmallIntegerField()
    hra3 = models.SmallIntegerField()
    hra4 = models.SmallIntegerField()
    hra5 = models.SmallIntegerField()
    def get_avg(self):
        return (self.hra1+self.hra2+self.hra3+self.hra4+self.hra5)/5
    hra_assessment_report = models.TextField() 

class DHassessment(models.Model):
    assessedby = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created1')
    assessedof = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created')
    dha1 = models.SmallIntegerField()
    dha2 = models.SmallIntegerField()
    dha3 = models.SmallIntegerField()
    dha4 = models.SmallIntegerField()
    dha5 = models.SmallIntegerField()
    def get_avg(self):
        return (self.dha1+self.dha2+self.dha3+self.dha4+self.dha5)/5
    dha_assessment_report = models.TextField()  

class DTassessment(models.Model):
    assessedby = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created1')
    assessedof = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created')
    dta1 = models.SmallIntegerField()
    dta2 = models.SmallIntegerField()
    dta3 = models.SmallIntegerField()
    dta4 = models.SmallIntegerField()
    dta5 = models.SmallIntegerField()
    def get_avg(self):
        return (self.dta1+self.dta2+self.dta3+self.dta4+self.dta5)/5
    dta_assessment_report = models.TextField()          

class ManagementFB(models.Model):
    feedbackby = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created1')
    feedbackof = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created2')
    feedbackto = models.ForeignKey('User',on_delete = models.CASCADE,related_name='%(class)s_requests_created')
    mf1 = models.SmallIntegerField()
    mf2 = models.SmallIntegerField()
    mf3 = models.SmallIntegerField()
    mf4 = models.SmallIntegerField()
    mf5 = models.SmallIntegerField()
    def getavg(self):
        return (self.mf1+self.mf2+self.mf3+self.mf4+self.mf5)/5
    mfcomment = models.TextField()

class Client(models.Model):
    cname = models.TextField(max_length=50)
    pid = models.ForeignKey('Project',on_delete = models.CASCADE,related_name='%(class)s_requests_created')
    c1 = models.SmallIntegerField()
    c2 = models.SmallIntegerField()
    c3 = models.SmallIntegerField()

class Project(models.Model):
    pname = models.CharField(max_length=20)
    dno = models.ForeignKey('Dept',on_delete = models.CASCADE,related_name='%(class)s_requests_created')


class Report(models.Model):
    user_id = models.ForeignKey("User", related_name='%(class)s_requests_created1', on_delete=models.CASCADE)
    report = models.TextField() 