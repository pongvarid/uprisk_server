from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
 
admin.site.site_header = 'ระบบ แผนบริหารจัดการความเสี่ยงและควบคุมภายใน'
admin.site.register(AgencyType)
class AgencyAdmin(admin.ModelAdmin): 
    list_display = ('name','agency_type')
    list_filter = ('agency_type',)
    search_fields = ['name']
admin.site.register(Agency,AgencyAdmin)

class UserAdmin(admin.ModelAdmin): 
    autocomplete_fields = ['agency','user']  
    list_display = ('full_name','agency','register_type','status','supervisor','executive')
    list_filter = ('agency','status','supervisor','executive')
    search_fields = ['full_name']
admin.site.register(Profile,UserAdmin)

class RmPlanAdmin(admin.ModelAdmin): 
    filter_horizontal = ('mission',) 
    search_fields = ['name','year']
    list_filter = ('agency','strategic','strategy') 
admin.site.register(RmPlan,RmPlanAdmin)

admin.site.register(Year)
admin.site.register(Mission)
admin.site.register(Strategic)
admin.site.register(Strategy) 