from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    linkedin_profile = models.URLField(max_length=200, null=True)
    profile_description = models.TextField(null=True)

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()
        for _ in range(count):
            s = Teacher()
            s.first_name = faker.first_name()
            s.last_name = faker.last_name()
            s.linkedin_profile = f"{s.first_name}{s.last_name}@linkedin.com".lower()
            s.profile_description = faker.paragraph()

            s.save()

    def __str__(self):
        return f"Teacher({self.id}) {self.first_name} {self.last_name} " \
               f"{self.linkedin_profile} {self.profile_description}"
