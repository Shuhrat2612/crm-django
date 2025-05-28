# 1. Python bazasini olib kelamiz
FROM python:3.12-slim

# 2. Konteyner ichida ish katalogi
WORKDIR /app

# 3. Tizimga kerakli kutubxonalar
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && apt-get clean

# 4. Pythondagi kutubxonalar
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Loyihani konteynerga ko‘chirish
COPY . .

# 6. Static fayllarni yig‘ish
RUN python manage.py collectstatic --noinput || true

# 7. Gunicorn bilan ishga tushirish
CMD ["gunicorn", "crm.wsgi:application", "--bind", "0.0.0.0:8000"]