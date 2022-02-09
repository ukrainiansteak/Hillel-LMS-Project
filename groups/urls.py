from django.urls import path

from groups.views import get_group, list_groups

app_name = 'groups'

urlpatterns = [
    path('<int:id>', get_group, name='group'),
    path('', list_groups, name='list_groups'),
]