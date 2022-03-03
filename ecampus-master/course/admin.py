from django.contrib import admin

from .models import Course, StudentCourse, Material, Attendance

# Register your models here.

admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(Material)
admin.site.register(Attendance)
