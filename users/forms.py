from datetime import date
from .models import CustomUser, UserRolePermission
from django import forms
from django.contrib.auth.forms import UserCreationForm
from employees.models import Employee
from django.contrib.auth.models import Permission
from attendance.models import AttendanceRecord
import face_recognition
import base64
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    position = forms.CharField(max_length=100)
    hire_date = forms.DateField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    face_image = forms.CharField(widget=forms.HiddenInput(), required=True)  # Hidden field to store the base64 image

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'position', 'hire_date', 'phone_number', 'address', 'password1', 'password2', 'face_image')

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

            # Decode the base64 face image and process it
            face_image_data = self.cleaned_data['face_image']
            face_encoding = self.process_face_image(face_image_data)
            if face_encoding:
                employee.set_face_encoding(face_encoding)
                employee.save()
            
            # Assign permissions based on user role
            if user.user_role == 'superuser':
                permissions = Permission.objects.all()
            elif user.user_role == 'moderator':
                permissions = Permission.objects.filter(
                    codename__in=['view_employee', 'view_attendance', 'generate_report']
                )
            else:  # employee
                permissions = Permission.objects.filter(
                    codename__in=['view_own_details', 'view_own_attendance']
                )
            # Save role permissions to the database
            for permission in permissions:
                UserRolePermission.objects.create(user_role=user.user_role, permission=permission)
        return user

    def process_face_image(self, base64_data):
        try:
            # Decode the base64 image
            image_data = base64.b64decode(base64_data.split(',')[1])
            image = Image.open(BytesIO(image_data))

            # Convert the image to a format that face_recognition can use
            image = image.convert('RGB')
            image_array = face_recognition.load_image_file(BytesIO(image.tobytes()))

            # Find face encodings
            face_encodings = face_recognition.face_encodings(image_array)
            if face_encodings:
                return face_encodings[0]  # Return the first face encoding found
            return None
        except Exception as e:
            print(f"Error processing face image: {e}")
            return None
    

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