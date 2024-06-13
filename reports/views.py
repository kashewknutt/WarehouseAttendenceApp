from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from attendance.models import AttendanceRecord

@login_required
def attendance_report(request):
    if request.user.user_role not in ['moderator','superuser','employee']:
        messages.error(request, 'Unauthorized access.')
        return redirect('login')
    
    user_id = request.GET.get('user_id') 
    user = CustomUser.objects.get(id=user_id)
    attendance_records = AttendanceRecord.objects.filter(user=user)

    # Render the report template with the retrieved data
    return render(request, 'attendance_report.html', {
        'user': user,
        'attendance_records': attendance_records,
    })

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from attendance.models import AttendanceRecord

@login_required
def employee_attendance_report(request):
    if request.user.user_role not in ['moderator','superuser']:
        messages.error(request, 'Unauthorized access.')
        return redirect('login')
    # Retrieve attendance records for all employees
    employees = CustomUser.objects.filter(user_role='employee')
    attendance_data = []

    for employee in employees:
        attendance_records = AttendanceRecord.objects.filter(user=employee)
        attendance_data.append({
            'user': employee,
            'attendance_records': attendance_records,
        })

    # Render the report template with the retrieved data
    return render(request, 'employee_attendance_report.html', {
        'attendance_data': attendance_data,
    })

