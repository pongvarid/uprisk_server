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


admin.site.register(Year)
admin.site.register(Mission)

class ChoiceAdmin(admin.ModelAdmin):

    list_display = ('name','value')
    list_filter = ('name',)
    search_fields = ['name','value']
admin.site.register(Choice,ChoiceAdmin)

# admin.site.register(Strategic)
# admin.site.register(Strategy)
#
# admin.site.register(SOFCEG)
#
# class EffectOfRiskAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['agency',]
#     search_fields = ['name']
#     list_filter = ('agency',)
# admin.site.register(EffectOfRisk,EffectOfRiskAdmin)
#
# class RiskRMAdmin(admin.ModelAdmin):
#     # filter_horizontal = ('effect_risk',)
#     autocomplete_fields = ['rm_plan',]
#     search_fields = ['name',]
#     list_filter = ('name','rm_plan',)
# admin.site.register(RiskRM,RiskRMAdmin)
admin.site.register(RmPlan)
#
# class RmPlanInline(admin.StackedInline):
#     model = RiskRM
#     fk_name = "rm_plan"
#     # filter_horizontal = ('effect_risk',)
#
#     # filter_horizontal = ('choice',)
#     def get_extra(self, request, obj=None, **kwargs):
#         extra = 1
#         return extra
#
# class RmPlanAdmin(admin.ModelAdmin):
#     inlines = [RmPlanInline, ]
#     # filter_horizontal = ('mission',)
#     list_filter = ("agency", 'strategic', 'strategy',)
#     autocomplete_fields = ["agency",]
#     search_fields = ['name','year']
#
# admin.site.register(RmPlan,RmPlanAdmin)
