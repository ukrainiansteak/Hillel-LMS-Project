from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, DetailView

from groups.forms import GroupFilter, GroupUpdateForm
from groups.models import Group


class AllGroupsListView(LoginRequiredMixin, ListView):
    model = Group
    queryset = Group.objects.all()
    template_name = 'groups/list_groups.html'
    paginate_by = 10
    ordering = ['id']

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        filter_ = GroupFilter(self.request.GET, queryset=queryset)
        return filter_

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_ = GroupFilter(self.request.GET, queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        return context


class GroupListView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GroupEditView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'groups/edit_group.html'
    pk_url_kwarg = 'id'
