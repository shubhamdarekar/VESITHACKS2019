from django.contrib import admin
from .models import User,Dept,Evaluates,HRassessment,DHassessment,DTassessment,ManagementFB,Client,Project

# Register your models here.
admin.site.register(User)
admin.site.register(Dept)
admin.site.register(Evaluates)
admin.site.register(HRassessment)
admin.site.register(DHassessment)
admin.site.register(DTassessment)
admin.site.register(ManagementFB)
admin.site.register(Client)
admin.site.register(Project)


