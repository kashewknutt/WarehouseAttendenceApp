from django.db import models
from users.models import CustomUser
import json

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee_profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    employee_id = models.CharField(max_length=5, unique=True, editable=False)  # Unique 5-digit employee ID
    face_encoding = models.TextField(null=True, blank=True)  # Field to store facial encoding

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

    def set_face_encoding(self, encoding):
        self.face_encoding = json.dumps(encoding.tolist())

    def get_face_encoding(self):
        if self.face_encoding:
            return json.loads(self.face_encoding)
        return None

    def __str__(self):
        return f'{self.employee_id} - {self.first_name} {self.last_name}'
