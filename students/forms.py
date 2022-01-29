import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'(\+\d\d?)?\(\d{3}\)(\d-?){7}$', phone_number):
            raise ValidationError("Phone should be in format +1(111)111-11-11")
        return phone_number

    def clean(self):
        result = super().clean()
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']

        if enroll_date > graduate_date:
            raise ValidationError("Enroll date cannot be later"
                                  " than graduate date.")

        return result


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta:
        model = Student
        exclude = ['age']
