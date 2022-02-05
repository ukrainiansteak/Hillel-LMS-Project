from django.contrib import admin  # noqa

# Register your models here.
from teachers.models import Teacher

admin.site.register(Teacher)
