import django_filters

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from django.db import models
from teachers.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'profile_description',
                  'email', 'phone_number', 'birth_date']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        prohibited_domains = ['mail.ru', 'yandex.ru', 'rambler.ru']
        for domain in prohibited_domains:
            if domain in email.split('@')[1]:
                raise ValidationError(f"You cannot register a {domain} email.")

        qs = Teacher.objects.all().filter(email=email)
        if qs.exists():
            if self.instance in qs:
                return email
            else:
                raise ValidationError("Email is not unique.")

        return email


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    pass
