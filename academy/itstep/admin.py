from django.contrib import admin
from .models import Teacher, Course, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "date_of_birth", "user")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "start", "end")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "url", "date_of_birth")
    filter_horizontal = ("courses",)
