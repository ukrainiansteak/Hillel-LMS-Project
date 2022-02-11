from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Updates missing emails and phone numbers in students'

    def handle(self, *args, **options):
        Student.update_students()
        self.stdout.write(self.style.SUCCESS("Successfully updated students."))
