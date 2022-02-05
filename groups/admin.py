from django.contrib import admin  # noqa

# Register your models here.
from groups.models import Group

admin.site.register(Group)