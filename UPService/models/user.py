from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from UPService.models.general import *
# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name = _("ผู้ใช้")
        verbose_name_plural = _("ผู้ใช้") 
    ANSWERS = (
        ('microsoft.com','microsoft.com'),
        ('google.com','google.com'),
         ('facebook.com','facebook.com'),
        ('ปกติ', 'ปกติ'), 
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    register_type = models.CharField(max_length=255,choices=ANSWERS)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    supervisor = models.BooleanField(default=False,verbose_name="หัวหน้า (ระดับหน่วยงาน)")
    executive = models.BooleanField(default=False,verbose_name="หัวหน้า (ระดับมหาวิทยาลัย)")
    status = models.BooleanField(default=True,verbose_name="เปิดการใช้งาน")
    in_up = models.BooleanField(default=False,verbose_name="บุลคากรภายใน") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name 
 
    @property
    def full_name(self):
        return "%s %s %s"%(self.user.id, self.user.first_name, self.user.last_name)