from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=True)
    phone_number = models.CharField(
        null=True,
        max_length=24,
        validators=[
            RegexValidator(r'^(\+\d\d?)?\(\d{3}\)(\d-?){7}$',
                           message="Phone should be in format +1(111)222-33-44")
        ])
