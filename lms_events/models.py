from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=32)
    time = models.DateTimeField()


class EventHomeworkComplete(Event):
    student = models.ForeignKey(
        to='students.Student',
        on_delete=models.CASCADE,
        related_name='+'
    )
    lecture = models.ForeignKey(
        to='students.Lecture',
        on_delete=models.CASCADE,
        related_name='+'
    )
