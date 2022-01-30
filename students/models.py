import datetime

from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from faker import Faker
import random

from core_lms.validators import even_integer_validator


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(
        default=20,
        validators=[
            MinValueValidator(20),
            MaxValueValidator(120),
            even_integer_validator
        ])
    email = models.EmailField(max_length=64)
    phone_number = models.CharField(
        max_length=24,
        validators=[
            RegexValidator(r'^(\+\d\d?)?\(\d{3}\)(\d-?){7}$',
                           message="Phone should be in format +1(111)222-33-44")
        ])
    enroll_date = models.DateField(default=datetime.datetime.today())
    graduate_date = models.DateField(default=datetime.datetime.today)

    @classmethod
    def generate_students(cls, count):
        faker = Faker()
        for _ in range(count):
            s = Student()
            s.first_name = faker.first_name()
            s.last_name = faker.last_name()
            s.age = random.randint(18, 80)

            s.save()

    def __str__(self):
        return f"Student({self.id}) {self.first_name} " \
               f"{self.last_name} {self.age} {self.phone_number} {self.email}"
