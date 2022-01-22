from django.http import HttpResponse
from django.shortcuts import render  # noqa

# Create your views here.
from lms.utils import render_list, filter_queryset
from students.models import Student


def get_students(request):
    qs = Student.objects.all()
    params = [
        'first_name',
        'first_name__startswith',
        'first_name__endswith',
        'first_name__contains',
        'last_name',
        'last_name__startswith',
        'last_name__endswith',
        'last_name__contains',
        'age',
        'age__gt'
        'age__lt'
    ]

    try:
        qs = filter_queryset(request, qs, params)
    except ValueError as e:
        return HttpResponse(str(e), status=400)

    return render_list(qs)
