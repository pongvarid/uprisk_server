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
    mission = models.ManyToManyField(Mission,verbose_name="การบริหารจัดการความเสี่ยงตามพันธกิจ")
    strategic = models.ForeignKey(Strategic, on_delete=models.CASCADE,blank=True, null=True,verbose_name="ยุทธศาสตร์")
    target_value = models.CharField(max_length=255, null=True,blank=True,verbose_name="ค่าเป้าหมาย")
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE,blank=True, null=True,verbose_name="กลยุทธ์")
    strategy_other = models.CharField(max_length=255, null=True,blank=True,verbose_name="กลยุทธ์อื่นๆ") 
    signature = models.CharField(max_length=999, null=True,blank=True,verbose_name="ลายมือชื่อ")
    sign = models.CharField(max_length=255, null=True,blank=True,verbose_name="ลงชื่อ")
    position = models.CharField(max_length=255, null=True,blank=True,verbose_name="ตําแหน่ง")
    date = models.DateField(max_length=255, null=True,blank=True,verbose_name="วันที่")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.agency.name

class SOFCEG(models.Model):
    class Meta:
        verbose_name = _("ประเภทความเสี่ยง ")
        verbose_name_plural = _("ประเภทความเสี่ยง ")
    name = models.CharField(max_length=255,verbose_name="หัวข้อประเภทความเสี่ยง ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class EffectOfRisk(models.Model):
    class Meta:
        verbose_name = _("ผลกระทบของความเสี่ยง")
        verbose_name_plural = _("ผลกระทบของความเสี่ยง")
    name = models.CharField(max_length=255,verbose_name="หัวข้อผลกระทบของความเสี่ยง")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE,verbose_name="หน่วยงาน", blank=True,null=True )
    year = models.ForeignKey(Year, on_delete=models.CASCADE,blank=True, null=True,verbose_name="ปีงบประมาณ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "("+self.agency.fullname+")"+ " " +self.name

class RiskRM(models.Model):
    class Meta:
        verbose_name = _("ตารางความเสี่ยง")
        verbose_name_plural = _("ตารางความเสี่ยง")
    rm_plan = models.ForeignKey(RmPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name="ความเสี่ยง")
    sofceg = models.ForeignKey(SOFCEG, on_delete=models.CASCADE,verbose_name="ประเภทความเสี่ยง (S-O-F-C-E-G)" )
    internal_cause = models.CharField(max_length=255,verbose_name="ปัจจัยภายใน", blank=True,null=True)
    external_cause = models.CharField(max_length=255, verbose_name="ปัจจัยภายนอก", blank=True,null=True)
    effect_risk = models.ManyToManyField(EffectOfRisk, verbose_name="ผลกระทบของความเสี่ยง" )
    existing_control = models.CharField(max_length=255,verbose_name="การควบคุมที่มีอยู่ในปัจจุบัน", blank=True,null=True)
    risk_management_measures = models.CharField(max_length=255, verbose_name="มาตรการจัดการความเสี่ยง", blank=True,null=True)
    kri = models.CharField(max_length=255, verbose_name="ดัชนีชี้วัดความเสี่ยง(KRI)", blank=True,null=True)
    responsible = models.CharField(max_length=255, verbose_name="ผู้รับผิดชอบ", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

