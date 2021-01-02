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