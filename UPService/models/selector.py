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

class Strategic(models.Model):
    class Meta:
        verbose_name = _("ยุทธศาสตร์")
        verbose_name_plural = _("ยุทธศาสตร์") 
    name = models.CharField(max_length=255,verbose_name="หัวข้อยุทธศาสตร์")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Strategy(models.Model):
    class Meta:
        verbose_name = _("กลยุทธ์")
        verbose_name_plural = _("กลยุทธ์") 
    name = models.CharField(max_length=255,verbose_name="หัวข้อกลยุทธ์")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True, verbose_name="หน่วยงาน")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

