import datetime

from django.db import models
from faker import Faker
import random


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(default=20)
    email = models.EmailField(max_length=64)
    phone_number = models.CharField(max_length=24)
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
