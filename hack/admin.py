# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Attendance_Sheet)
admin.site.register(Total_No_of_Classes)
admin.site.register(Info_of_allocation)