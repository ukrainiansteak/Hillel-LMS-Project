from django.shortcuts import render  # noqa


def index(request):
    return render(request, 'index.html')
