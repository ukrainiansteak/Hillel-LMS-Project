from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa

from django.views.decorators.csrf import csrf_exempt

from core_lms.utils import filter_queryset, render_teachers_list_html
from teachers.forms import TeacherCreateForm, TeacherUpdateForm
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    params = [
        'first_name',
        'last_name',
        'profile_description',
        'phone_number',
        'email',
    ]

    form = f"""<form>
            <p>Search teachers</p>
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
                <input type="text" name="profile_description" 
                    value="{request.GET.get('profile_description', '')}"
                    placeholder="Input Profile Description">
            </p>
            <p>
                <input type="text" name="email" 
                    value="{request.GET.get('email', '')}"
                    placeholder="Input Email">
            </p>
            <p>
                <input type="text" name="phone_number" 
                    value="{request.GET.get('phone_number', '')}"
                    placeholder="Input Phone Number">
            </p>
            <p>
                <input type="date" name="birth_date" 
                    value="{request.GET.get('birth_date', '')}"
                    placeholder="Input Birth Date">
            </p>
            <p><button type="submit">Search</button></p>
        </form>
        <a href="/teachers/create">Add new teacher</a>
        <br>
        """

    try:
        qs = filter_queryset(request, qs, params)
    except ValueError as e:
        return HttpResponse(str(e), status=400)
    qs = qs.order_by('-id')
    return render_teachers_list_html(qs[:10], form)


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers')
    else:
        form = TeacherCreateForm()

    html = f"""
            <form method="post">
                {form.as_p()}
                <p><button type="submit">Create Teacher</button></p>
            </form>
        """
    return HttpResponse(html)


@csrf_exempt
def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers')
    else:
        form = TeacherUpdateForm(instance=teacher)

    html = f"""
            <form method="post">
                {form.as_p()}
                <p><button type="submit">Update Teacher</button></p>
            </form>
        """
    return HttpResponse(html)


