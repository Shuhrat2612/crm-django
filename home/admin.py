from django.contrib import admin
from .models import Customer, Lead, Deal, Task, Note

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'phone', 'assigned_to', 'created_at')
    list_filter = ('created_at', 'assigned_to')
    search_fields = ('name', 'email', 'company', 'phone')
    date_hierarchy = 'created_at'

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'source', 'assigned_to', 'created_at')
    list_filter = ('status', 'source', 'assigned_to', 'created_at')
    search_fields = ('customer__name', 'customer__email', 'notes')
    date_hierarchy = 'created_at'

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'lead', 'value', 'status', 'expected_close_date', 'assigned_to')
    list_filter = ('status', 'assigned_to', 'expected_close_date')
    search_fields = ('title', 'lead__customer__name', 'notes')
    date_hierarchy = 'expected_close_date'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'due_date', 'assigned_to', 'customer', 'deal')
    list_filter = ('priority', 'status', 'assigned_to', 'due_date')
    search_fields = ('title', 'description', 'customer__name', 'deal__title')
    date_hierarchy = 'due_date'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'customer', 'deal', 'created_at')
    list_filter = ('created_by', 'created_at')
    search_fields = ('content', 'customer__name', 'deal__title')
    date_hierarchy = 'created_at'
