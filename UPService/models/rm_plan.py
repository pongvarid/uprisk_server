from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from UPService.models.general import *
from UPService.models.user import *
from UPService.models.selector import * 

class RmPlan(models.Model):
    class Meta:
        verbose_name = _("แผนบริหารจัดการความเสี่ยงและควบคุมภายใน (RM-Plan)")
        verbose_name_plural = _("แผนบริหารจัดการความเสี่ยงและควบคุมภายใน (RM-Plan)") 
    year = models.ForeignKey(Year, on_delete=models.CASCADE,blank=True, null=True,verbose_name="ปีงบประมาณ")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE,blank=True, null=True,verbose_name="หน่วยงาน")
    mission = models.ForeignKey(Mission,on_delete=models.CASCADE, verbose_name="การบริหารจัดการความเสี่ยงตามพันธกิจ")
    strategic = models.TextField(blank=True, null=True,verbose_name="ยุทธศาสตร์")
    target_value = models.CharField(max_length=255, null=True,blank=True,verbose_name="ค่าเป้าหมาย")
    strategy = models.TextField( blank=True, null=True,verbose_name="กลยุทธ์")
    signature = models.TextField( null=True,blank=True,verbose_name="ลายมือชื่อ")
    sign = models.CharField(max_length=255, null=True,blank=True,verbose_name="ลงชื่อ")
    position = models.CharField(max_length=255, null=True,blank=True,verbose_name="ตําแหน่ง")
    date = models.DateField(max_length=255, null=True,blank=True,verbose_name="วันที่")
    type = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        try:
            return self.agency.name
        except:
            return "ไม่ระบุ"




class RiskRM(models.Model):
    class Meta:
        verbose_name = _("ตารางความเสี่ยง")
        verbose_name_plural = _("ตารางความเสี่ยง")
    rm_plan = models.ForeignKey(RmPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name="ความเสี่ยง",blank=True, null=True,)
    sofceg = models.TextField(verbose_name="ประเภทความเสี่ยง (S-O-F-C-E-G)" ,blank=True, null=True,)
    internal_cause = models.TextField(verbose_name="ปัจจัยภายใน", blank=True,null=True)
    external_cause = models.TextField(verbose_name="ปัจจัยภายนอก", blank=True,null=True)
    effect_risk = models.TextField(verbose_name="ผลกระทบของความเสี่ยง" ,blank=True, null=True,)
    existing_control = models.TextField(verbose_name="การควบคุมที่มีอยู่ในปัจจุบัน", blank=True,null=True)
    risk_management_measures = models.TextField( verbose_name="มาตรการจัดการความเสี่ยง", blank=True,null=True)
    kri = models.TextField( verbose_name="ดัชนีชี้วัดความเสี่ยง(KRI)", blank=True,null=True)
    responsible = models.CharField(max_length=255, verbose_name="ผู้รับผิดชอบ", blank=True,null=True)
    response_date = models.DateField( verbose_name="ดำเนินการ", blank=True, null=True)
    l = models.CharField(max_length=255, verbose_name="โอกาส", blank=True, null=True)
    i = models.CharField(max_length=255, verbose_name="ผลกระทบ", blank=True, null=True)
    li_score = models.CharField(max_length=255, verbose_name="โอกาสxผลกระทบ ผลลัพธ์", blank=True, null=True)
    li_result = models.CharField(max_length=255, verbose_name="โอกาสxผลกระทบ ความหมาย", blank=True, null=True)
    l1 = models.CharField(max_length=255, verbose_name="l1", blank=True, null=True)
    l2 = models.CharField(max_length=255, verbose_name="l2", blank=True, null=True)
    l3 = models.CharField(max_length=255, verbose_name="l3", blank=True, null=True)
    l4 = models.CharField(max_length=255, verbose_name="l4", blank=True, null=True)
    l5 = models.CharField(max_length=255, verbose_name="l5", blank=True, null=True)
    i1 = models.CharField(max_length=255, verbose_name="i1", blank=True, null=True)
    i2 = models.CharField(max_length=255, verbose_name="i2", blank=True, null=True)
    i3 = models.CharField(max_length=255, verbose_name="i3", blank=True, null=True)
    i4 = models.CharField(max_length=255, verbose_name="i4", blank=True, null=True)
    i5 = models.CharField(max_length=255, verbose_name="i5", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class RiskRMR6(models.Model):
    class Meta:
        verbose_name = _("ตารางความเสี่ยง")
        verbose_name_plural = _("ตารางความเสี่ยง")
    rm_plan = models.ForeignKey(RmPlan, on_delete=models.CASCADE)
    rm_risk = models.ForeignKey(RiskRM,  on_delete=models.CASCADE ,blank=True, null=True)
    rm_risk_result = models.TextField(verbose_name="ผลเดิม" ,blank=True, null=True,)
    name = models.CharField(max_length=255,verbose_name="ความเสี่ยง",blank=True, null=True,)  
    responsible = models.CharField(max_length=255, verbose_name="ผู้รับผิดชอบ", blank=True,null=True) 
    rm6_manager = models.TextField(verbose_name="ดำเนินงานในรอบ 6 เดือน" ,blank=True, null=True,)
    rm6_result = models.TextField(verbose_name="ผลการดำเนินงานในรอบ 6 เดือน" ,blank=True, null=True,)
    l = models.CharField(max_length=255, verbose_name="โอกาส", blank=True, null=True)
    i = models.CharField(max_length=255, verbose_name="ผลกระทบ", blank=True, null=True)
    li_score = models.CharField(max_length=255, verbose_name="โอกาสxผลกระทบ ผลลัพธ์", blank=True, null=True)
    li_result = models.CharField(max_length=255, verbose_name="โอกาสxผลกระทบ ความหมาย", blank=True, null=True)
    l1 = models.CharField(max_length=255, verbose_name="l1", blank=True, null=True)
    l2 = models.CharField(max_length=255, verbose_name="l2", blank=True, null=True)
    l3 = models.CharField(max_length=255, verbose_name="l3", blank=True, null=True)
    l4 = models.CharField(max_length=255, verbose_name="l4", blank=True, null=True)
    l5 = models.CharField(max_length=255, verbose_name="l5", blank=True, null=True)
    i1 = models.CharField(max_length=255, verbose_name="i1", blank=True, null=True)
    i2 = models.CharField(max_length=255, verbose_name="i2", blank=True, null=True)
    i3 = models.CharField(max_length=255, verbose_name="i3", blank=True, null=True)
    i4 = models.CharField(max_length=255, verbose_name="i4", blank=True, null=True)
    i5 = models.CharField(max_length=255, verbose_name="i5", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class RiskRMR12(models.Model):
    class Meta:
        verbose_name = _("ตารางความเสี่ยง")
        verbose_name_plural = _("ตารางความเสี่ยง")
    rm_plan = models.ForeignKey(RmPlan, on_delete=models.CASCADE)
    rm6_risk = models.ForeignKey(RiskRMR6,  on_delete=models.CASCADE ,blank=True, null=True)
    rm_risk_result = models.TextField(verbose_name="ผลเดิม" ,blank=True, null=True,)
    name = models.CharField(max_length=255,verbose_name="ความเสี่ยง",blank=True, null=True,)  
    responsible = models.CharField(max_length=255, verbose_name="ผู้รับผิดชอบ", blank=True,null=True) 
    rm6_manager = models.TextField(verbose_name="ดำเนินงานในรอบ 6 เดือน" ,blank=True, null=True,)
    rm6_result = models.TextField(verbose_name="ผลการดำเนินงานในรอบ 6 เดือน" ,blank=True, null=True,)
    l = models.CharField(max_length=255, verbose_name="โอกาส", blank=True, null=True)
    i = models.CharField(max_length=255, verbose_name="ผลกระทบ", blank=True, null=True)
    li_score = models.CharField(max_length=255, verbose_name="โอกาสxผลกระทบ ผลลัพธ์", blank=True, null=True)
    li_result = models.CharField(max_length=255, verbose_name="โอกาสxผลกระทบ ความหมาย", blank=True, null=True)
    l1 = models.CharField(max_length=255, verbose_name="l1", blank=True, null=True)
    l2 = models.CharField(max_length=255, verbose_name="l2", blank=True, null=True)
    l3 = models.CharField(max_length=255, verbose_name="l3", blank=True, null=True)
    l4 = models.CharField(max_length=255, verbose_name="l4", blank=True, null=True)
    l5 = models.CharField(max_length=255, verbose_name="l5", blank=True, null=True)
    i1 = models.CharField(max_length=255, verbose_name="i1", blank=True, null=True)
    i2 = models.CharField(max_length=255, verbose_name="i2", blank=True, null=True)
    i3 = models.CharField(max_length=255, verbose_name="i3", blank=True, null=True)
    i4 = models.CharField(max_length=255, verbose_name="i4", blank=True, null=True)
    i5 = models.CharField(max_length=255, verbose_name="i5", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
