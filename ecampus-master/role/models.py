from django.db import models

# Create your models here.
class Role(models.Model):
    roleId = models.IntegerField(primary_key=True)
    roleName = models.CharField(max_length=50)
    class Meta: 
        verbose_name_plural = "Role"


class User(models.Model):
    UserId = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length=50)
    email = models.EmailField()
    #password = models.CharField(max_length=20, widget=forms.PasswordInput)
    roleId = models.ForeignKey('role.Role',on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "User"