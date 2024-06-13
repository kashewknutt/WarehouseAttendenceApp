from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserRolePermission
from employees.models import Employee
from django.contrib.auth.models import Permission
from attendance.models import AttendanceRecord
import face_recognition

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    position = forms.CharField(max_length=100)
    hire_date = forms.DateField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'position', 'hire_date', 'phone_number', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
            user.set_password(self.cleaned_data['password1'])  # Properly hash and save password
            user.save()
            
            # Create corresponding Employee object
            employee = Employee.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                position=self.cleaned_data['position'],
                hire_date=self.cleaned_data['hire_date'],
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )

            # Capture facial data and store in Employee model
            image_path = 'path_to_uploaded_image'  # Replace with actual path to uploaded image
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]  # Assuming one face per image
            employee.facial_data = encoding.tobytes()
            employee.save()

        return user  

class RecordAttendanceForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label="Employee")
    check_in_time = forms.TimeField(required=False, label="Check In Time")
    check_out_time = forms.TimeField(required=False, label="Check Out Time")

    class Meta:
        model = AttendanceRecord
        fields = ['employee', 'check_in_time', 'check_out_time']

    def save(self, commit=True):
        # Use date.today() to get today's date
        today = date.today()

        # Get or create the attendance record for the employee on today's date
        attendance_record, created = AttendanceRecord.objects.get_or_create(
            user=self.cleaned_data['employee'].user,
            date=today  # Use today's date
        )

        # Update the check-in and check-out times if provided
        if self.cleaned_data['check_in_time']:
            attendance_record.check_in_time = self.cleaned_data['check_in_time']
        if self.cleaned_data['check_out_time']:
            attendance_record.check_out_time = self.cleaned_data['check_out_time']

        # Save the attendance record if commit is True
        if commit:
            attendance_record.save()

        return attendance_record