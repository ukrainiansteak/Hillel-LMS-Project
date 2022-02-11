import django_filters
from django.db import models
from django.forms import ModelForm

from groups.models import Group


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = ['date_start', 'location', 'specialty']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['headman'].queryset = self.fields['headman'].queryset.filter(
            group_id=self.instance.id
        )
