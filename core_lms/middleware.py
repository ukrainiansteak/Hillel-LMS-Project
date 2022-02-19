import time

from core_lms.models import Logger


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        response.headers['X-Response-Time'] = str(round(time.time() - start, 2))
        return response


class PerfTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        execution_time = time.time() - start
        log = Logger()
        if request.user.is_authenticated:
            log.user = request.user
        else:
            log.user = None
        log.path = request.path
        log.execution_time = execution_time
        if request.META['QUERY_STRING']:
            log.query_params = request.META['QUERY_STRING']
        else:
            log.query_params = None
        log.save()

        return response
