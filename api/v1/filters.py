import django_filters

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['gte', 'lte', 'exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'location': ['icontains'],
            'specialty': ['icontains'],
        }
