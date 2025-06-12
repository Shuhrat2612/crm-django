from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    path('customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer-edit'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    path('leads/', views.LeadListView.as_view(), name='leads-list'),
    path('leads/add/', views.LeadCreateView.as_view(), name='leads-add'),
    path('leads/<int:pk>/edit/', views.LeadUpdateView.as_view(), name='leads-edit'),
    path('leads/<int:pk>/delete/', views.LeadDeleteView.as_view(), name='leads-delete'),
    path('deals/', views.DealListView.as_view(), name='deals-list'),
    path('deals/add/', views.DealCreateView.as_view(), name='deals-add'),
    path('deals/edit/<int:pk>/', views.DealUpdateView.as_view(), name='deals-edit'),
    path('deals/delete/<int:pk>/', views.DealDeleteView.as_view(), name='deals-delete'),
    path('tasks/', views.TaskListView.as_view(), name='tasks-list'),
    path('task/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('notes/', views.NoteListView.as_view(), name='notes-list'),
    path('notes/add/', views.NoteCreateView.as_view(), name='notes-add'),
    path('tasks/edit/<int:pk>/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
] 