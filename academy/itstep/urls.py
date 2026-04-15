from django.urls import path
from .views import teacher_list, course_list, student_list

urlpatterns = [
    path("teachers/", teacher_list, name="teacher_list"),
    path("courses/", course_list, name="course_list"),
    path("students/", student_list, name="student_list"),
]
