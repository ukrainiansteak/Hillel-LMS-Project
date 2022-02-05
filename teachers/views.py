from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()

    qs = qs.order_by('-id')
    teachers_filter = TeacherFilter(data=request.GET, queryset=qs)
    return render(request, 'teachers/list_teachers.html', {
        'filter': teachers_filter,
    })


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherCreateForm()

    return render(request, 'teachers/create_teacher.html', {
        'form': form
    })


def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherUpdateForm(instance=teacher)

    return render(request, 'teachers/edit_teacher.html', {
        'form': form
    })


def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list_teachers'))

    return render(request, 'teachers/delete_teacher.html', {
        'teacher': teacher
    })
