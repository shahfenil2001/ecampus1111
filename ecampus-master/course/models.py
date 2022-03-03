from ast import Interactive
from pyexpat import model
from tabnanny import verbose
from telnetlib import STATUS
from tkinter import ACTIVE
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Course(models.Model):
    courseId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseDescription = models.TextField()
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )  
    
    active = models.IntegerField(default=0, choices=STATUS)
    class Meta: 
        verbose_name_plural = "Course"

class StudentCourse(models.Model):
    studentCourseId = models.IntegerField(primary_key=True)
    courseId = models.ForeignKey('course.Course',on_delete=models.CASCADE)
    UserId = models.ForeignKey('role.User',on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "StudentCourse"

class Material(models.Model):
    batchId = models.ManyToManyField('batch.Batch')
    courseId = models.ForeignKey('course.Course', on_delete=models.CASCADE, blank= True, null=True)
    materialTitle = models.CharField(max_length=50, null=True)
    materialDescription = models.TextField(null=True)
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )  
    
    active = models.IntegerField(default=0, choices=STATUS)
    materialURL = models.URLField(null=True)
    class Meta: 
        verbose_name_plural = "Material"

class Attendance(models.Model):
    attendanceId = models.IntegerField(primary_key=True)
    batchId = models.ForeignKey('batch.Batch', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta: 
        verbose_name_plural = "Attendance"