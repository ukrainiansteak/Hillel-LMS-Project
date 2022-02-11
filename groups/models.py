import datetime
import random

from django.db import models
from django.urls import reverse
from faker import Faker


class Group(models.Model):
    LOCATION_CHOICES = [
        ("O", "Online"),
        ("KY", "Kyiv"),
        ("KH", "Kharkiv"),
        ("OD", "Odesa"),
        ("DN", "Dnipro"),
    ]

    date_start = models.DateField()
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=True)
    specialty = models.CharField(max_length=60, null=False)
    headman = models.OneToOneField(
        to='students.Student',
        null=True,
        related_name='headed_group',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"Group {self.specialty} {self.get_location_display()} {self.date_start}"

    @classmethod
    def generate(cls, count):
        faker = Faker()
        for _ in range(count):
            group = Group()
            group.specialty = faker.job()
            group.location = random.choice(cls.LOCATION_CHOICES)[0]
            group.date_start = (
                    datetime.datetime.now() -
                    datetime.timedelta(days=random.randint(1, 1000))
            )
            group.save()

    def get_absolute_url(self):
        return reverse('groups:group', kwargs={'id': self.id})
