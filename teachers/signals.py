import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from teachers.models import Teacher


logger = logging.getLogger("mylogger")


@receiver(post_save, sender=Teacher)
def print_create_message(sender, instance, created, **kwargs):
    if created:
        logger.info("Teacher profile created successfully.")
