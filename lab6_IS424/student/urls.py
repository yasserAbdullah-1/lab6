from django.urls import path
from . import views
app_name="lab6"
urlpatterns = [
    path('courses', views.courses, name='courses'),
    path('students',views.students,name='students'),
    path("<int:student_id>",views.details,name="details"),
    path("<int:student_id>/enrollInCoures",views.enrollInCoures,name="enrollInCoures")
   
]