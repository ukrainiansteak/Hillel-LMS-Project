from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student

import django_filters


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):
        result = super().clean()
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']

        if enroll_date > graduate_date:
            raise ValidationError("Enroll date cannot be later"
                                  " than graduate date.")

        return result

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        has_phone_number_qs = Student.objects.filter(phone_number=phone_number)
        if self.instance:
            has_phone_number_qs = has_phone_number_qs.exclude(
                id=self.instance.id
            )

        if has_phone_number_qs.exists():
            raise ValidationError("Phone number is not unique.")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']
        prohibited_domains = ['mail.ru', 'yandex.ru', 'rambler.ru']
        for domain in prohibited_domains:
            if domain in email.split('@')[1]:
                raise ValidationError(f"You cannot register a {domain} email.")

        qs = Student.objects.all().filter(email=email)
        if qs.exists():
            if self.instance in qs:
                return email
            else:
                raise ValidationError("Email is not unique.")

        return email


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta:
        model = Student
        exclude = ['age']
