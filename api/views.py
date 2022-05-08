from rest_framework import viewsets

from api.serializers import StudentSerializer, TeacherSerializer, GroupSerializer
from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
