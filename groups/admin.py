from django.contrib import admin  # noqa

# Register your models here.
from groups.models import Group
from students.models import Student


class StudentTable(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name']
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'specialty']
    inlines = [StudentTable]
    list_editable = ['specialty']
    autocomplete_fields = ['headman',]


admin.site.register(Group, GroupAdmin)
