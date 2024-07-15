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

        # Delete all existing employees
        Employee.objects.all().delete()

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

        # Initialize lists to keep track of employees at each level
        vps = []
        initiative_leads = []
        department_managers = []
        team_leads = []
        senior_staffs = []

        # Level 2: VPs
        for _ in range(5):
            vp = Employee.objects.create(
                first_name=seeder.faker.first_name(),
                last_name=seeder.faker.last_name(),
                position='VP',
                date_of_hire=timezone.now(),
                email=unique_email(),
                manager=ceo
            )
            vps.append(vp)

        # Level 3: Initiative Leads
        for vp in vps:
            for _ in range(7):
                initiative_lead = Employee.objects.create(
                    first_name=seeder.faker.first_name(),
                    last_name=seeder.faker.last_name(),
                    position='Initiative Lead',
                    date_of_hire=timezone.now(),
                    email=unique_email(),
                    manager=vp
                )
                initiative_leads.append(initiative_lead)

        # Level 4: Department Managers
        for initiative_lead in initiative_leads:
            for _ in range(7):
                department_manager = Employee.objects.create(
                    first_name=seeder.faker.first_name(),
                    last_name=seeder.faker.last_name(),
                    position='Department Manager',
                    date_of_hire=timezone.now(),
                    email=unique_email(),
                    manager=initiative_lead
                )
                department_managers.append(department_manager)

        # Level 5: Team Leads
        for department_manager in department_managers:
            for _ in range(7):
                team_lead = Employee.objects.create(
                    first_name=seeder.faker.first_name(),
                    last_name=seeder.faker.last_name(),
                    position='Team Lead',
                    date_of_hire=timezone.now(),
                    email=unique_email(),
                    manager=department_manager
                )
                team_leads.append(team_lead)

        # Level 6: Senior Staff
        for team_lead in team_leads:
            for _ in range(7):
                senior_staff = Employee.objects.create(
                    first_name=seeder.faker.first_name(),
                    last_name=seeder.faker.last_name(),
                    position='Senior Staff',
                    date_of_hire=timezone.now(),
                    email=unique_email(),
                    manager=team_lead
                )
                senior_staffs.append(senior_staff)

        # Level 7: Staff
        for senior_staff in senior_staffs:
            for _ in range(5):
                Employee.objects.create(
                    first_name=seeder.faker.first_name(),
                    last_name=seeder.faker.last_name(),
                    position='Staff',
                    date_of_hire=timezone.now(),
                    email=unique_email(),
                    manager=senior_staff
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with employees.'))
