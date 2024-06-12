# attendance/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from employees.models import Employee
from .models import AttendanceRecord

def check_in(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    AttendanceRecord.objects.create(
        employee=employee,
        check_in_time=timezone.now(),
        date=timezone.now().date()
    )
    return redirect('employee_detail', pk=employee.id)

def check_out(request, record_id):
    record = get_object_or_404(AttendanceRecord, id=record_id)
    record.check_out_time = timezone.now()
    record.save()
    return redirect('employee_detail', pk=record.employee.id)
