from django.urls import path

from students.views import StudentEditView, StudentDeleteView, StudentCreateView, StudentListView

app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='list_students'),
    path('create', StudentCreateView.as_view(), name='create_student'),
    path('update/<int:id>', StudentEditView.as_view(), name='update_student'),
    path('delete/<int:id>', StudentDeleteView.as_view(), name='delete_student'),
    ]
