from django.db import models
from faker import Faker

from core_lms.models import Person


class Teacher(Person):
    profile_description = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    group = models.ForeignKey(
        to='groups.Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='teachers'
    )

    class Role(models.TextChoices):
        MENTOR = 'M', 'Mentor'
        TEACHER = 'T', 'Teacher'

    role = models.CharField(default=Role.TEACHER,
                            choices=Role.choices,
                            max_length=1)

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()
        for _ in range(count):
            t = Teacher()
            t.first_name = faker.first_name()
            t.last_name = faker.last_name()
            t.profile_description = faker.paragraph()
            t.email = faker.email()
            t.birth_date = faker.date_of_birth()
            t.phone_number = faker.phone_number()

            t.save()

    def __str__(self):
        return f"Teacher({self.id}) {self.first_name} {self.last_name} " \
               f"{self.email} {self.birth_date}, {self.phone_number}"

    def name(self):
        return f'{self.first_name} {self.last_name}'
