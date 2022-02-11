from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


class StudentListView(ListView):
    model = Student
    paginate_by = 10
    template_name = 'students/list_students.html'
    queryset = Student.objects.all().\
        select_related('group__headman').order_by('-id')

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = StudentFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students_filter = StudentFilter(queryset=self.queryset)
        context['filter'] = students_filter
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list_students')
    template_name = 'students/create_student.html'


class StudentEditView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentUpdateForm
    template_name = 'students/edit_student.html'
    pk_url_kwarg = 'id'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    template_name = 'students/delete_student.html'
    pk_url_kwarg = 'id'
