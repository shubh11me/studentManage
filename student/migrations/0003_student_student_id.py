# Generated by Django 3.2.8 on 2022-06-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_std'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
