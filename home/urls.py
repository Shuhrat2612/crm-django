from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    path('leads/', views.LeadListView.as_view(), name='leads-list'),
    path('leads/add/', views.LeadCreateView.as_view(), name='leads-add'),
    path('deals/', views.DealListView.as_view(), name='deals-list'),
    path('deals/add/', views.DealCreateView.as_view(), name='deals-add'),
    path('tasks/', views.TaskListView.as_view(), name='tasks-list'),
    path('task/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('notes/', views.NoteListView.as_view(), name='notes-list'),
    path('notes/add/', views.NoteCreateView.as_view(), name='notes-add'),
] 