from django import forms
from .models import Task, Lead, Deal
from django.contrib.admin import widgets

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status', 'customer', 'deal', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'deal': forms.Select(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['customer', 'status', 'source', 'notes', 'assigned_to']
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Customer'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'source': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter lead source'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter any additional notes'
            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-control'
            })
        }

class DealForm(forms.ModelForm):
    expected_close_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        ),
        required=False
    )

    class Meta:
        model = Deal
        fields = ['lead', 'title', 'value', 'status', 'expected_close_date', 'notes', 'assigned_to']
        widgets = {
            'lead': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Lead'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter deal title'
            }),
            'value': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter deal value'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter deal notes'
            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-control'
            })
        } 