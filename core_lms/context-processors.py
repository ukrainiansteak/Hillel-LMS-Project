import datetime
import math


def pi(request):
    return {
        'pi': math.pi
    }


def current_time(request):
    return {
        'time': datetime.datetime.now
    }
