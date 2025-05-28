from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Customer, Lead, Deal, Task, Note
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm, LeadForm, DealForm
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
import json
from django.utils import timezone

# Create your views here.

@login_required
def dashboard(request):
    # Basic counts
    context = {
        'customers_count': Customer.objects.count(),
        'leads_count': Lead.objects.count(),
        'deals_count': Deal.objects.count(),
        'tasks_count': Task.objects.count(),
        'recent_tasks': Task.objects.order_by('-created_at')[:5],
        'recent_deals': Deal.objects.order_by('-created_at')[:5],
    }
    
    # Leads by status for pie chart
    leads_by_status = Lead.objects.values('status').annotate(count=Count('id'))
    context['leads_status_labels'] = json.dumps([status['status'] for status in leads_by_status])
    context['leads_status_data'] = json.dumps([status['count'] for status in leads_by_status])
    
    # Deals value by month for line chart
    six_months_ago = timezone.now() - timedelta(days=180)
    deals_by_month = Deal.objects.filter(
        created_at__gte=six_months_ago
    ).annotate(
        month=TruncMonth('created_at')
    ).values('month').annotate(
        total_value=Sum('value')
    ).order_by('month')
    
    # Format dates and ensure all months are included
    months = []
    values = []
    current = six_months_ago.replace(day=1)
    end = timezone.now()
    
    # Create a dictionary of existing data
    data_dict = {d['month'].strftime('%B %Y'): float(d['total_value'] or 0) for d in deals_by_month}
    
    # Fill in all months
    while current <= end:
        month_str = current.strftime('%B %Y')
        months.append(month_str)
        values.append(data_dict.get(month_str, 0))
        current = (current + timedelta(days=32)).replace(day=1)
    
    context['deals_months'] = json.dumps(months)
    context['deals_values'] = json.dumps(values)
    
    # Tasks by priority for bar chart
    tasks_by_priority = Task.objects.values('priority').annotate(count=Count('id'))
    context['tasks_priority_labels'] = json.dumps([t['priority'] for t in tasks_by_priority])
    context['tasks_priority_data'] = json.dumps([t['count'] for t in tasks_by_priority])
    
    # Deals by status for doughnut chart
    deals_by_status = Deal.objects.values('status').annotate(count=Count('id'))
    context['deals_status_labels'] = json.dumps([d['status'] for d in deals_by_status])
    context['deals_status_counts'] = json.dumps([d['count'] for d in deals_by_status])
    
    return render(request, 'home/dashboard.html', context)

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'home/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'home/customer_form.html'
    fields = ['name', 'email', 'phone', 'company', 'address', 'assigned_to']
    success_url = reverse_lazy('customer-list')

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'home/leads_list.html'
    context_object_name = 'leads'
    paginate_by = 10

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'home/leads_form.html'
    success_url = reverse_lazy('leads-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Lead'
        return context

class DealListView(LoginRequiredMixin, ListView):
    model = Deal
    template_name = 'home/deals_list.html'
    context_object_name = 'deals'
    paginate_by = 10

class DealCreateView(LoginRequiredMixin, CreateView):
    model = Deal
    form_class = DealForm
    template_name = 'home/deals_form.html'
    success_url = reverse_lazy('deals-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Deal'
        return context

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'home/tasks_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'home/tasks_form.html'
    success_url = reverse_lazy('tasks-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Task'
        return context

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'home/notes_list.html'
    context_object_name = 'notes'
    paginate_by = 10

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'home/notes_form.html'
    fields = ['content', 'customer', 'deal', 'created_by']
    success_url = reverse_lazy('notes-list')
