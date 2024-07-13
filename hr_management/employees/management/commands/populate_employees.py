# employees/management/commands/seed_employees.py

import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from employees.models import Employee
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seed the database with sample employees'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        used_emails = set()
        # Create CEO
        ceo_email = "ceo@example.com"
        ceo = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            position="CEO",
            date_of_hire=timezone.now(),
            email=ceo_email
        )
        used_emails.add(ceo_email)

        def unique_email():
            while True:
                email = seeder.faker.email()
                if email not in used_emails:
                    used_emails.add(email)
                    return email

        # Seed other employees
        for _ in range(49999):
            seeder.add_entity(Employee, 1, {
                'first_name': lambda x: seeder.faker.name(),
                'last_name': lambda x: seeder.faker.name(),
                'position': lambda x: random.choice(
                    ["VP", "Manager", "Team Lead", "Senior Developer", "Developer", "Junior Developer"]),
                'date_of_hire': lambda x: timezone.now(),
                'email': lambda x: unique_email(),
                'manager': lambda x: Employee.objects.order_by('?').first()
            })
        print("executing....")
        seeder.execute()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with employees.'))
