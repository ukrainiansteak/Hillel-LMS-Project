from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets

from api.v1.filters import StudentFilter
from api.v1.pagination import StudentPagination
from api.v1.serializers import StudentSerializer, TeacherSerializer, GroupSerializer
from api.v1.throttles import AnonStudentThrottle
from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = StudentFilter
    ordering_fields = ['id', 'age', 'first_name', 'last_name']
    throttle_classes = [AnonStudentThrottle]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
