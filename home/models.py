from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    name = models.CharField(_('Customer Name'), max_length=200)
    email = models.EmailField(_('Email'), unique=True)
    phone = models.CharField(_('Phone'), max_length=20, blank=True)
    company = models.CharField(_('Company'), max_length=200, blank=True)
    address = models.TextField(_('Address'), blank=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_customers')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', _('New')),
        ('contacted', _('Contacted')),
        ('qualified', _('Qualified')),
        ('unqualified', _('Unqualified')),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='leads')
    status = models.CharField(_('Status'), max_length=20, choices=STATUS_CHOICES, default='new')
    source = models.CharField(_('Source'), max_length=100, blank=True)
    notes = models.TextField(_('Notes'), blank=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_leads')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.customer.name} - {self.get_status_display()}"

class Deal(models.Model):
    STATUS_CHOICES = [
        ('proposal', _('Proposal')),
        ('negotiation', _('Negotiation')),
        ('won', _('Won')),
        ('lost', _('Lost')),
    ]
    
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='deals')
    title = models.CharField(_('Deal Title'), max_length=200)
    value = models.DecimalField(_('Value'), max_digits=10, decimal_places=2)
    status = models.CharField(_('Status'), max_length=20, choices=STATUS_CHOICES, default='proposal')
    expected_close_date = models.DateField(_('Expected Close Date'), null=True, blank=True)
    notes = models.TextField(_('Notes'), blank=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_deals')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    deal = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_priority_color(self):
        colors = {
            'low': 'info',
            'medium': 'warning',
            'high': 'danger'
        }
        return colors.get(self.priority, 'secondary')

    def get_status_color(self):
        colors = {
            'pending': 'warning',
            'in_progress': 'info',
            'completed': 'success',
            'cancelled': 'danger'
        }
        return colors.get(self.status, 'secondary')

class Note(models.Model):
    content = models.TextField(_('Content'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='deal_notes', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Note by {self.created_by.username} on {self.created_at.strftime('%Y-%m-%d')}"
