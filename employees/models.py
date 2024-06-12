# employees/models.py

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    employee_id = models.CharField(max_length=5, unique=True, editable=False)  # Unique 5-digit employee ID

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate ID for new employees
            last_employee = Employee.objects.order_by('-employee_id').first()
            if last_employee:
                last_id = int(last_employee.employee_id)
                new_id = last_id + 1
                self.employee_id = f'{new_id:05d}'
            else:
                self.employee_id = '00001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee_id} - {self.first_name} {self.last_name}'