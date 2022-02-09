from django.contrib import admin  # noqa

# Register your models here.
from core_lms.models import TaggedItem, Tag

admin.site.register(TaggedItem)
admin.site.register(Tag)
