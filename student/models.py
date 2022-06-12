from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.CharField(max_length=200,default=' ')
    name = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    std= models.IntegerField()


class teacher(models.Model):
    teacher_name=models.CharField(max_length=200)
    teacher_age=models.CharField(max_length=200)
    teacher_email=models.CharField(max_length=200)

    
class Meta:
    db_table = 'student'