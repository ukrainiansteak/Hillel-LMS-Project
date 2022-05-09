from rest_framework.throttling import AnonRateThrottle


class AnonStudentThrottle(AnonRateThrottle):
    scope = 'students'
