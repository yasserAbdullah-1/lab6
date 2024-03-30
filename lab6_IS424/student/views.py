from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student.models import *


class studentModelForm(forms.ModelForm):
    class Meta:
        model=stud
        fields="__all__"   
        
class coursesModelForm(forms.ModelForm):
    class Meta:
        model=course
        fields="__all__"               
   


def students(request):
    students=stud.objects.all()
    if request.method=="POST":
        forms=studentModelForm(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request,'nameIT/addS.html',{"form":studentModelForm(),'students':students})     
        
    return render(request,'nameIT/addS.html',{"form":studentModelForm(),'students':students})   
    
    
    
def courses(request):
    coursee=course.objects.all()
    if request.method=="POST":
        formc=coursesModelForm(request.POST)
        if formc.is_valid():
            formc.save()
            return render(request,'nameIT/addC.html',{"courses":coursee,'form':coursesModelForm()})
               
    return render(request,'nameIT/addC.html',{"courses":coursee,'form':coursesModelForm()})   
    
    
def details(request,student_id):        
    studentInfo=stud.objects.get(id=student_id)
    registeredcourses=studentInfo.courses.all()
    notRegisteredCourse=course.objects.exclude(students=studentInfo).all()
    return render(request,"nameIT/details.html",{"id":student_id,"studnent":studentInfo,"notRegisteredCourse":notRegisteredCourse,"registeredcourses":registeredcourses})

# def index(request):
    
#     return render(request,"nameIT/details.html",{"studnents":stud.object.all()})
     
def enrollInCoures(request,student_id):
    if request.method=="POST":
        student=stud.objects.get(pk=student_id) 
        course_id=int(request.POST["course"])
        coursee=course.objects.get(id=course_id)#we want to get the details of that course
        coursee.students.add(student)
        studentInfo=stud.objects.get(id=student_id)
        registeredcourses=studentInfo.courses.all()
        notRegisteredCourse=course.objects.exclude(students=studentInfo).all()
        return render(request,"nameIT/details.html",{"id":student_id,"studnent":studentInfo,"notRegisteredCourse":notRegisteredCourse,"registeredcourses":registeredcourses})

    return render(request,"nameIT/details.html")
     
       