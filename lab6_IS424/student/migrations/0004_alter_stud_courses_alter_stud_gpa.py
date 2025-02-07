# Generated by Django 5.0.1 on 2024-03-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_stud_delete_student_rename_cid_course_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='student.course'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='gpa',
            field=models.FloatField(),
        ),
    ]
