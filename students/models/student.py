import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from faker import Faker
import random

from core_lms.models import Person


class Student(Person):
    age = models.IntegerField(
        default=20,
        validators=[
            MinValueValidator(20),
            MaxValueValidator(120),
        ])
    enroll_date = models.DateField(default=datetime.datetime.today)
    graduate_date = models.DateField(default=datetime.datetime.today)
    inn = models.PositiveIntegerField(unique=True, null=True)
    group = models.ForeignKey(
        to='groups.Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='students'
    )

    @classmethod
    def generate_students(cls, count):
        faker = Faker()
        for _ in range(count):
            s = Student()
            s.first_name = faker.first_name()
            s.last_name = faker.last_name()
            s.age = random.randint(18, 80)

            s.save()

    @classmethod
    def update_students(cls):
        faker = Faker()
        students = Student.objects.all()
        for s in students:
            if not s.email:
                s.email = faker.email()
            if not s.phone_number:
                s.phone_number = faker.phone_number()
            s.save()

    def __str__(self):
        return f"Student({self.id}) {self.first_name} " \
               f"{self.last_name} {self.age} {self.phone_number} {self.email}"

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
