from django.core.exceptions import ValidationError
from django.forms import ModelForm

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        prohibited_domains = ['mail.ru', 'yandex.ru', 'rambler.ru']
        for domain in prohibited_domains:
            if domain in email:
                raise ValidationError(f"You cannot register a {domain} email.")

        qs = Teacher.objects.all().filter(email=email)
        if qs.exists():
            if self.instance in qs:
                return email
            else:
                raise ValidationError(f"Email is not unique.")

        return email


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    pass
