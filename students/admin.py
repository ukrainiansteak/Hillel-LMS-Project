from django.contrib import admin

# Register your models here.
from students.models import Student, Lecture

admin.site.register(Student)
admin.site.register(Lecture)
