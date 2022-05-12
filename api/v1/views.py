from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets

from api.v1.filters import StudentFilter, TeacherFilter, GroupFilter
from api.v1.pagination import APIPagination
from api.v1.serializers import StudentSerializer, TeacherSerializer, GroupSerializer
from api.v1.throttles import AnonStudentThrottle
from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = APIPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = StudentFilter
    ordering_fields = ['id', 'age', 'first_name', 'last_name']
    search_fields = ['age', 'first_name', 'last_name']
    throttle_classes = [AnonStudentThrottle]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = APIPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = TeacherFilter
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['id', 'first_name', 'last_name']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = APIPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = GroupFilter
    ordering_fields = ['id', 'location', 'specialty']
    search_fields = ['location', 'specialty']
