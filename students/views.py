from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from lms.utils import render_list, filter_queryset, render_list_html, render_students_list_html
from students.forms import StudentCreateForm, StudentUpdateForm
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

    form = f"""<form>
            <p>Search students</p>
            <p>
                <input type="text" name="first_name" 
                    value="{request.GET.get('first_name', '')}" 
                    placeholder="Input First Name">
            </p>
            <p>
                <input type="text" name="last_name" 
                    value="{request.GET.get('last_name', '')}"
                    placeholder="Input Last Name">
            </p>
            <p>
                <input type="number" name="age" 
                    value="{request.GET.get('age', '')}"
                    placeholder="Input Age">
            </p>

            <p><button type="submit">Search</button></p>
        </form>
        <a href="/students/create">Add new student</a>
        <br>
        """

    try:
        qs = filter_queryset(request, qs, params)
    except ValueError as e:
        return HttpResponse(str(e), status=400)
    qs = qs.order_by('-id')
    return render_students_list_html(qs, form)


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')
    else:
        form = StudentCreateForm()

    html = f"""
            <form method="post">
                {form.as_p()}
                <p><button type="submit">Create Student</button></p>
            </form>
        """
    return HttpResponse(html)


@csrf_exempt
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')
    else:
        form = StudentUpdateForm(instance=student)

    html = f"""
            <form method="post">
                {form.as_p()}
                <p><button type="submit">Update Student</button></p>
            </form>
        """
    return HttpResponse(html)
