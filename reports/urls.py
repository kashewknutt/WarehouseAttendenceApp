from django.urls import path
from . import views

urlpatterns = [
    path('attendance-report/', views.attendance_report, name='attendance_report'),
    path('employee-attendance-report/', views.employee_attendance_report, name='employee_attendance_report'),
    # Add more URL patterns for other types of reports as needed
]
