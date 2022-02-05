from django.urls import path

from students.views import get_students, create_student, update_student, delete_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list_students'),
    path('create', create_student, name='create_student'),
    path('update/<int:id>', update_student, name='update_student'),
    path('delete/<int:id>', delete_student, name='delete_student'),
    ]
