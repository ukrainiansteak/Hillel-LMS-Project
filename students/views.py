from django.http import HttpResponseRedirect, HttpResponse  # noqa
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    qs = Student.objects.all()

    qs = qs.select_related('group__headman').order_by('-id')
    students_filter = StudentFilter(data=request.GET, queryset=qs)
    return render(request, 'students/list_students.html', {
        'filter': students_filter,
    })


def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list_students'))
    else:
        form = StudentCreateForm()

    return render(request, 'students/create_student.html', {
        'form': form
    })


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list_students'))
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list_students'))

    return render(request, 'students/delete_student.html', {
        'student': student
    })
