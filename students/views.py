from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from core_lms.utils import filter_queryset, render_students_list_html
from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    qs = Student.objects.all()

    qs = qs.order_by('-id')
    students_filter = StudentFilter(data=request.GET, queryset=qs)
    return render(request, 'list_students.html', {
        'filter': students_filter,
        'args': request.GET,
    })


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_students'))
    else:
        form = StudentCreateForm()

    return render(request, 'create_student.html', {
        'form': form
    })


@csrf_exempt
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_students'))
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'edit_student.html', {
        'form': form
    })
