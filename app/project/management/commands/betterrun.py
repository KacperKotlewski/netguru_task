from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    help = "migrate, collect statics and runserver <ip:port>"

    def add_arguments(self, parser):
        super().add_arguments(parser)

    def handle(self, *args, **options):
        call_command("migrate", interactive=False)
        call_command("collectstatic", interactive=False)
        return super().handle(*args, **options)
