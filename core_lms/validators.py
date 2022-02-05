from django.core.exceptions import ValidationError  # noqa


def even_integer_validator(value):
    if value % 2 == 1:
        raise ValidationError("Value should be even")
