from django.core.management.base import BaseCommand, CommandError

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates teachers'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        if options['count'] > 0:
            Teacher.generate_teachers(options['count'])
            self.stdout.write(self.style.SUCCESS(f"Successfully generated {options['count']} teachers."))
        else:
            raise CommandError(f"Cannot generate {options['count']} teachers.")
