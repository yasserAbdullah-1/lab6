

from django.db import models

# Create your models here.
class course(models.Model): 
    cname=models.CharField(max_length=64)
    precourses=models.CharField(max_length=64)
    capacity=models.IntegerField()  
    def __str__(self):
        return f"course name:{self.cname} requirements: {self.precourses} course capacity:{self.capacity}" 
    
class stud(models.Model):
    fname=models.CharField(max_length=64)
    Lname=models.CharField(max_length=64)
    sid=models.IntegerField()
    gpa=models.FloatField()
    def __str__(self):
        return f"first name:{self.fname} last name: {self.Lname} ID:{self.sid} GPA:{self.gpa}"
    courses=models.ManyToManyField(course,blank=False,related_name='students')
    
