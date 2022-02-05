from django.db import models


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

    def __str__(self):
        return f"Group {self.specialty} {self.location} {self.date_start}"
