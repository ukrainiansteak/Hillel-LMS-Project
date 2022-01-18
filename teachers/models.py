from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    linkedin_profile = models.URLField(max_length=200, null=True)
    profile_description = models.TextField(null=True)
