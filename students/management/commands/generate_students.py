from django.core.management.base import BaseCommand, CommandError

from students.models import Student


class Command(BaseCommand):
    help = 'Generates students'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        if options['count'] > 0:
            Student.generate_students(options['count'])
            self.stdout.write(self.style.SUCCESS(f"Successfully generated {options['count']} students."))
        else:
            raise CommandError(f"Cannot generate {options['count']} students.")
