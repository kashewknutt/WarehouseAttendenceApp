from django.db import models
from employees.models import Employee  # Import the Employee model from the employees app

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Link to Employee
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)  # Optional if not checked out yet
    date = models.DateField()

    def __str__(self):
        return f'{self.employee.name} - {self.date}'