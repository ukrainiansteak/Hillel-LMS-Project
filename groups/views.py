from django.views.generic import UpdateView, ListView, DetailView

from groups.forms import GroupFilter, GroupUpdateForm
from groups.models import Group


class AllGroupsListView(ListView):
    model = Group
    queryset = Group.objects.all()
    template_name = 'groups/list_groups.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = GroupFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        groups_filter = GroupFilter(queryset=self.queryset)
        context['filter'] = groups_filter
        return context


class GroupListView(DetailView):
    model = Group
    template_name = 'groups/group.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GroupEditView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'groups/edit_group.html'
    pk_url_kwarg = 'id'
