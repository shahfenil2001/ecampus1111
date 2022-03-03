from django.db import models

# Create your models here.
class Batch(models.Model):
    batchId = models.IntegerField(primary_key=True)
    courseId = models.ForeignKey('course.Course',on_delete=models.CASCADE, blank=True, null=True)
    batchName = models.CharField(max_length=50)
    batchdescription = models.CharField(max_length=50)
    #facultyId = models.ForeignKey('faculty.Faculty',on_delete=models.CASCADE)
    batchStartDate = models.DateField()
    batchEndDate = models.DateField()
    class Meta: 
        verbose_name_plural = "Batch"

class BatchDetail(models.Model):
    batch_detail_id = models.IntegerField(primary_key=True)
    batchId = models.OneToOneField(Batch, on_delete=models.CASCADE, blank=True, null=True)
    #studentId = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "BatchDetails"
    
class BatchTime(models.Model):
    batchTimeId = models.IntegerField(primary_key=True)
    batchId = models.ManyToManyField('batch.Batch')
    batchDay = models.DateField()
    BatchTime = models.TimeField()
    BatchDuration = models.DurationField()
    class Meta: 
        verbose_name_plural = "BatchTime"



