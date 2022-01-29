from django.http import HttpResponse
import html


def render_list(list_of_objects, extra_data="", no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_objects:
        string_rows.append(str(obj))

    message = "\n".join(string_rows)
    if not message:
        message = no_data_message
    response = HttpResponse(message)
    response.headers['Content-Type'] = 'text/plain'
    return response


def render_list_html(list_of_objects, extra_data="", no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_objects:
        string_rows.append(html.escape(str(obj)))

    message = "<br>".join(string_rows)
    if not list_of_objects:
        message += "<br>" + html.escape(no_data_message)
    response = HttpResponse(message)
    return response


def filter_queryset(request, qs, params):
    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            query[param_name + '__contains'] = str(param_value)

    try:
        qs = qs.filter(**query)
    except ValueError:
        raise ValueError("Error. Wrong input")

    return qs


def render_students_list_html(list_of_objects, extra_data="", no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_objects:
        string_rows.append(
            html.escape(str(obj)) + ' ' +
            f'<a href="/students/update/{obj.id}">Edit</a>'
            )

    message = "<br>".join(string_rows)
    if not list_of_objects:
        message += "<br>" + html.escape(no_data_message)
    response = HttpResponse(message)
    return response


def render_teachers_list_html(list_of_objects, extra_data="", no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_objects:
        string_rows.append(
            html.escape(str(obj)) + ' ' +
            f'<a href="/teachers/update/{obj.id}">Edit</a>'
            )

    message = "<br>".join(string_rows)
    if not list_of_objects:
        message += "<br>" + html.escape(no_data_message)
    response = HttpResponse(message)
    return response
