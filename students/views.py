from django.http import HttpResponse
from django.shortcuts import render  # noqa

# Create your views here.
from lms.utils import render_list
from students.models import Student


def get_students(request):
    qs = Student.objects.all()
    params = [
        'first_name',
        'first_name__startswith',
        'first_name__endswith',
        'first_name__contains',
        'last_name',
        'age',
        'age__gt'
        'age__lt'
    ]

    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            query[param_name] = param_value

    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error. Wrong input data, {str(e)}", status=400)

    return render_list(qs)
