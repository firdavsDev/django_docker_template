import yaml
from django.core.management.base import BaseCommand, CommandError

from ...models import User


class Command(BaseCommand):
    help = "Import users from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import users... wait...",
            )
        )
        User.objects.all().delete()
        try:
            with open(
                "src/apps/common/fixtures/users.yml",
                "r",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    User.objects.create(
                        email=item["fields"]["email"],
                        password=item["fields"]["password"],
                        role = item["fields"]["role"],
                    )
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File users yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} users successfully imported"))
