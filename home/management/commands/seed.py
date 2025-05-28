from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from home.models import Customer, Lead, Deal, Task
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generates fake data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create test user if not exists
        try:
            test_user = User.objects.get(username='testuser')
        except User.DoesNotExist:
            test_user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
            self.stdout.write(self.style.SUCCESS('Created test user'))

        # Generate 100 customers
        customers = []
        for _ in range(100):
            customer = Customer.objects.create(
                name=fake.company(),
                email=fake.email(),
                phone=fake.phone_number(),
                company=fake.company(),
                address=fake.address(),
                assigned_to=test_user
            )
            customers.append(customer)
        self.stdout.write(self.style.SUCCESS('Created 100 customers'))

        # Generate leads
        lead_statuses = ['New', 'Contacted', 'Qualified', 'Lost', 'Won']
        leads = []
        for customer in customers:
            lead = Lead.objects.create(
                customer=customer,
                status=random.choice(lead_statuses),
                source=random.choice(['Website', 'Referral', 'Social Media', 'Email Campaign', 'Trade Show']),
                notes=fake.text(),
                assigned_to=test_user
            )
            leads.append(lead)
        self.stdout.write(self.style.SUCCESS('Created leads for customers'))

        # Generate deals
        deal_statuses = ['Pending', 'Won', 'Lost', 'Negotiating']
        for lead in leads[:70]:  # Create deals for 70% of leads
            Deal.objects.create(
                lead=lead,
                title=f"Deal for {lead.customer.name}",
                value=random.randint(1000, 100000),
                status=random.choice(deal_statuses),
                expected_close_date=datetime.now() + timedelta(days=random.randint(1, 90)),
                notes=fake.text(),
                assigned_to=test_user
            )
        self.stdout.write(self.style.SUCCESS('Created deals'))

        # Generate tasks
        task_priorities = ['High', 'Medium', 'Low']
        task_statuses = ['Pending', 'In Progress', 'Completed', 'Delayed']
        
        for _ in range(150):  # Create 150 tasks
            customer = random.choice(customers)
            deal = Deal.objects.filter(lead__customer=customer).first()
            
            Task.objects.create(
                title=fake.sentence(),
                description=fake.text(),
                due_date=datetime.now() + timedelta(days=random.randint(-10, 30)),
                priority=random.choice(task_priorities),
                status=random.choice(task_statuses),
                customer=customer,
                deal=deal,
                assigned_to=test_user
            )
        self.stdout.write(self.style.SUCCESS('Created tasks'))

        self.stdout.write(self.style.SUCCESS('Successfully generated all fake data')) 