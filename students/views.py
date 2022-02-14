from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    paginate_by = 10
    template_name = 'students/list_students.html'

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        filter_ = StudentFilter(self.request.GET, queryset=queryset)
        return filter_

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('group__headman').order_by('-id')
        filter_ = StudentFilter(self.request.GET, queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list_students')
    template_name = 'students/create_student.html'


class StudentEditView(LoginRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentUpdateForm
    template_name = 'students/edit_student.html'
    pk_url_kwarg = 'id'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    template_name = 'students/delete_student.html'
    pk_url_kwarg = 'id'
