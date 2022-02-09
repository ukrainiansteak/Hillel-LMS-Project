from django.shortcuts import render, get_object_or_404  # noqa

from groups.forms import GroupFilter
from groups.models import Group


def get_group(request, id):
    group = get_object_or_404(Group, id=id)
    return render(request, 'groups/group.html',
                  {'group': group})


def list_groups(request):
    qs = Group.objects.all()
    groups_filter = GroupFilter(data=request.GET, queryset=qs)
    return render(request, 'groups/list_groups.html', {
        'filter': groups_filter,
    })
