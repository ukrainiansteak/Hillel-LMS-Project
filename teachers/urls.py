from django.urls import path

from teachers.views import get_teachers, create_teacher, update_teacher, delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list_teachers'),
    path('create', create_teacher, name='create_teacher'),
    path('delete/<int:id>', delete_teacher, name='delete_teacher'),
    path('update/<int:id>', update_teacher, name='update_teacher'),
    ]
