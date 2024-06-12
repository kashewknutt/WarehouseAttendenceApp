from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserRolePermission
from employees.models import Employee

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
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                position=self.cleaned_data['position'],
                hire_date=self.cleaned_data['hire_date'],
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )
            # Assign permissions based on user role
            if user.user_role == 'superuser':
                permissions = permission.objects.all()
            elif user.user_role == 'moderator':
                permissions = permission.objects.filter(
                    codename__in=['view_employee', 'view_attendance', 'generate_report']
                )
            else:  # employee
                permissions = permission.objects.filter(
                    codename__in=['view_own_details', 'view_own_attendance']
                )
            # Save role permissions to the database
            for permission in permissions:
                UserRolePermission.objects.create(user_role=user.user_role, permission=permission)
        return user
