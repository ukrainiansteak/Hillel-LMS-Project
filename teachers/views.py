from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()

    qs = qs.order_by('-id')
    teachers_filter = TeacherFilter(data=request.GET, queryset=qs)
    return render(request, 'list_teachers.html', {
        'filter': teachers_filter,
        'args': request.GET,
    })


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_teachers'))
    else:
        form = TeacherCreateForm()

    return render(request, 'create_teacher.html', {
        'form': form
    })


@csrf_exempt
def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_teachers'))
    else:
        form = TeacherUpdateForm(instance=teacher)

    return render(request, 'edit_teacher.html', {
        'form': form
    })
