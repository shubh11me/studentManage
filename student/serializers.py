
from rest_framework import serializers

from .models import student,teacher

class studSeri(serializers.ModelSerializer):
    class Meta:
      model=student
      fields=('id','student_id','name','division','std')

class teachSeri(serializers.ModelSerializer):
    class Meta:
      model=teacher
      fields=('teacher_name','teacher_age','teacher_email')