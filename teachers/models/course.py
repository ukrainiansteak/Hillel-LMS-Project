from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=32)
    teachers = models.ManyToManyField(
        to='teachers.Teacher',
        related_name='courses',
    )
