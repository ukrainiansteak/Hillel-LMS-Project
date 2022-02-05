import datetime

from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from faker import Faker
import random


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(
        default=20,
        validators=[
            MinValueValidator(20),
            MaxValueValidator(120),
        ])
    email = models.EmailField(max_length=64)
    phone_number = models.CharField(
        max_length=24,
        validators=[
            RegexValidator(r'^(\+\d\d?)?\(\d{3}\)(\d-?){7}$',
                           message="Phone should be in format +1(111)222-33-44")
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
