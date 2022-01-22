from django.http import HttpResponse


def render_list(list_of_objects):
    string_rows = []
    for obj in list_of_objects:
        string_rows.append(str(obj))

    response = HttpResponse("\n".join(string_rows))
    response.headers['Content-Type'] = 'text/plain'
    return response


def filter_queryset(request, qs, params):
    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            query[param_name] = param_value
    try:
        qs = qs.filter(**query)
    except ValueError:
        raise ValueError("Error. Wrong input")

    return qs
