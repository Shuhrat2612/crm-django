import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")
django.setup()

from home.models import Customer, Lead, Deal, Task, Note
from django.contrib.auth.models import User

fake = Faker()
users = list(User.objects.all())
if not users:
    print("⚠️ Foydalanuvchi topilmadi! Avval `User` yarating.")
    exit()

clothing_sources = ['Online Store', 'Instagram', 'Physical Store', 'Referral', 'TikTok']
deal_titles = ['Summer Sale', 'Winter Clearance', 'Buy 1 Get 1', 'New Collection Offer']
clothing_products = ['Denim Jacket', 'T-Shirt', 'Hoodie', 'Sneakers', 'Sweatpants', 'Dress', 'Coat', 'Cap']

for _ in range(15):
    customer = Customer.objects.create(
        name=fake.name(),
        email=fake.unique.email(),
        phone=fake.phone_number(),
        company=random.choice(['', fake.company()]),  # Ba'zilari kompaniyasiz bo'lishi mumkin
        address=fake.address(),
        assigned_to=random.choice(users)
    )

    lead = Lead.objects.create(
        customer=customer,
        status=random.choice(['new', 'contacted', 'qualified', 'unqualified']),
        source=random.choice(clothing_sources),
        notes=f"{random.choice(clothing_products)} haqida qiziqish bildirildi.",
        assigned_to=random.choice(users)
    )

    deal = Deal.objects.create(
        lead=lead,
        title=random.choice(deal_titles),
        value=round(random.uniform(150_000, 1_200_000), 2),  # so'mda ifodalayotgandek
        status=random.choice(['proposal', 'negotiation', 'won', 'lost']),
        expected_close_date=fake.date_this_year(),
        notes="Maxsus chegirma yoki aksiyaga oid bitim.",
        assigned_to=random.choice(users)
    )

    task = Task.objects.create(
        title=f"{random.choice(clothing_products)} yetkazib berish",
        description="Yetkazib berish manzili bo‘yicha kuryer topshirilishi kerak.",
        due_date=fake.future_datetime(end_date="+7d"),
        priority=random.choice(['low', 'medium', 'high']),
        status=random.choice(['pending', 'in_progress', 'completed', 'cancelled']),
        customer=customer,
        deal=deal,
        assigned_to=random.choice(users)
    )

    note = Note.objects.create(
        content=f"{deal.title} bo‘yicha xizmat ko‘rsatildi.",
        customer=customer,
        deal=deal,
        created_by=random.choice(users)
    )

print("✅ 15 ta kiyim-kechak asosidagi fake CRM ma'lumotlar muvaffaqiyatli yaratildi.")
