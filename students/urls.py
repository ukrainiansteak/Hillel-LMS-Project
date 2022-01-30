from django.urls import path, include

from students.views import get_students, create_student, update_student

urlpatterns = [
    path('', get_students, name='list_students'),
    path('create', create_student, name='create_student'),
    path('update/<int:id>', update_student, name='update_student'),
    ]
