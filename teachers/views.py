from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list_teachers.html'
    paginate_by = 10
    ordering = ['-id']

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        filter_ = TeacherFilter(self.request.GET, queryset=queryset)
        return filter_

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('group')
        filter_ = TeacherFilter(self.request.GET, queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/create_teacher.html'
    form_class = TeacherCreateForm


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/edit_teacher.html'
    form_class = TeacherUpdateForm
    pk_url_kwarg = 'id'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/delete_teacher.html'
    pk_url_kwarg = 'id'
