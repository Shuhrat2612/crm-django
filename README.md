# CRM System

A modern Customer Relationship Management (CRM) system built with Django and Jinja2 templates.

## Features

- User Authentication and Authorization
- Customer Management
- Lead Management
- Task Management
- Basic Analytics
- Modern Responsive UI with Bootstrap 5
- Dashboard with Charts and Statistics

## Project Structure

```
crm-system/
├── backend/           # Django project
│   ├── crm/          # Main project settings
│   ├── accounts/     # User authentication
│   ├── customers/    # Customer management
│   ├── leads/        # Lead management
│   ├── tasks/        # Task management
│   ├── dashboard/    # Dashboard and analytics
│   ├── templates/    # Jinja2 templates
│   ├── static/       # Static files (CSS, JS, images)
│   └── requirements.txt
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r backend/requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Technologies Used

- Backend:
  - Django
  - Jinja2 Templates
  - PostgreSQL
  - Bootstrap 5
  - Django Crispy Forms
  - Django AllAuth
  - Chart.js for Analytics

## Features in Detail

### Authentication
- User registration and login
- Password reset functionality
- User profile management
- Role-based access control

### Customer Management
- Add, edit, and delete customers
- Customer details and history
- Customer categorization
- Contact information management

### Lead Management
- Track potential customers
- Lead status and priority
- Lead conversion tracking
- Lead assignment to team members

### Task Management
- Create and assign tasks
- Task status tracking
- Due date management
- Task categories and priorities

### Dashboard
- Overview of key metrics
- Recent activities
- Sales pipeline visualization
- Task completion statistics
- Lead conversion rates

## API Documentation

The API documentation will be available at `http://localhost:8000/api/docs/` when running the backend server. 