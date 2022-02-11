from django.urls import path

from groups.views import GroupEditView, AllGroupsListView, GroupListView

app_name = 'groups'

urlpatterns = [
    path('<int:id>', GroupListView.as_view(), name='group'),
    path('update/<int:id>', GroupEditView.as_view(), name='edit_group'),
    path('', AllGroupsListView.as_view(), name='list_groups'),
]
