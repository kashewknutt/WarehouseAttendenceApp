# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_registration, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/superuser/', views.superuser_dashboard, name='superuser_dashboard'),
    path('dashboard/moderator/', views.moderator_dashboard, name='moderator_dashboard'),
    path('dashboard/employee/', views.employee_dashboard, name='employee_dashboard'),
]
