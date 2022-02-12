from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


class TeachersListView(ListView):
    model = Teacher
    queryset = Teacher.objects.all().select_related('group')
    template_name = 'teachers/list_teachers.html'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = TeacherFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher_filter = TeacherFilter(self.request.GET, queryset=self.queryset)
        context['filter'] = teacher_filter
        return context


class TeacherCreateView(CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/create_teacher.html'
    form_class = TeacherCreateForm


class TeacherUpdateView(UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/edit_teacher.html'
    form_class = TeacherUpdateForm
    pk_url_kwarg = 'id'


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/delete_teacher.html'
    pk_url_kwarg = 'id'
