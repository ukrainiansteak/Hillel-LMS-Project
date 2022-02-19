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

    class DifficultyLevel(models.IntegerChoices):
        BASIC = 1, 'Low'
        NORMAL = 2, 'Normal'
        ADVANCED = 3, 'High'

    level = models.PositiveIntegerField(default=DifficultyLevel.BASIC,
                                        choices=DifficultyLevel.choices)
