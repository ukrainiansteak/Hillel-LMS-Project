from django.core.exceptions import ValidationError


def even_integer_validator(value):
    if value % 2 == 1:
        raise ValidationError("Value should be even")
