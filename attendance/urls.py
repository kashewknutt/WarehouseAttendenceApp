# attendance/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('check_in/<int:employee_id>/', views.check_in, name='check_in'),
    path('check_out/<int:record_id>/', views.check_out, name='check_out'),
]
