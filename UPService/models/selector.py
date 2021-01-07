from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from UPService.models.general import *

class Year(models.Model):
    class Meta:
        verbose_name = _("ปีงบประมาณ")
        verbose_name_plural = _("ปีงบประมาณ") 
    name = models.CharField(max_length=255,verbose_name="ปี")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Mission(models.Model):
    class Meta:
        verbose_name = _("พันธกิจ")
        verbose_name_plural = _("พันธกิจ") 
    name = models.CharField(max_length=255,verbose_name="หัวข้อพันธกิจ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Choice(models.Model):
    class Meta:
        verbose_name = _("ตัวเลือก")
        verbose_name_plural = _("ตัวเลือก")

    ANSWERS = (
        ('ยุทธศาสตร์', 'ยุทธศาสตร์'),
        ('กลยุทธ์', 'กลยุทธ์'),
        ('ประเภทความเสี่ยง', 'ประเภทความเสี่ยง'),
        ('ผลกระทบความเสี่ยง', 'ผลกระทบความเสี่ยง'),
        ('มาตรการจัดการความเสี่ยง', 'มาตรการจัดการความเสี่ยง'),
        ('ดัชนีวัดความเสี่ยง', 'ดัชนีวัดความเสี่ยง'),
        ('ปัจจัยภายใน', 'ปัจจัยภายใน'),
        ('ปัจจัยภายนอก', 'ปัจจัยภายนอก'),
    )
    name = models.CharField(max_length=255,choices=ANSWERS, verbose_name="หัวข้อตัวเลือก")
    value = models.CharField(max_length=255, verbose_name="รายการ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


