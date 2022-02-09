from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=32, null=False)
    students = models.ManyToManyField(
        to='students.Student',
        related_name='lectures'
    )
    groups = models.ForeignKey(
        to='groups.Group',
        on_delete=models.CASCADE
    )
