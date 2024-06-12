import os
import django
import random
from datetime import date, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouseApp.settings')
django.setup()

from users.forms import RegistrationForm
from users.models import CustomUser
from employees.models import Employee

def generate_random_date(start, end):
    """Generate a random date between start and end."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def create_user(username, first_name, last_name, email, position, hire_date, phone_number, address, password, user_role):
    """Create and save a user using the RegistrationForm."""
    form_data = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'position': position,
        'hire_date': hire_date,
        'phone_number': phone_number,
        'address': address,
        'password1': password,
        'password2': password,
    }
    form = RegistrationForm(data=form_data)
    if form.is_valid():
        user = form.save(commit=False)
        user.user_role = user_role
        user.set_password(form.cleaned_data['password1'])  # Properly hash the password
        user.save()

        # Create and link the Employee object
        employee = Employee.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            position=position,
            hire_date=hire_date,
            phone_number=phone_number,
            address=address
        )
        
        print(f'Successfully created {user_role}: {username}')
    else:
        print(f'Error creating user {username}:', form.errors)

# Generate and create 10 employees
for i in range(1, 11):
    create_user(
        username=f'employee{i}',
        first_name=f'EmployeeFirstName{i}',
        last_name=f'EmployeeLastName{i}',
        email=f'employee{i}@example.com',
        position='Warehouse Worker',
        hire_date=generate_random_date(date(2010, 1, 1), date.today()),
        phone_number=f'555-010{i}',
        address=f'Employee {i} Address',
        password='defaultpassword',
        user_role='employee'
    )

# Generate and create 5 moderators
for i in range(1, 6):
    create_user(
        username=f'moderator{i}',
        first_name=f'ModeratorFirstName{i}',
        last_name=f'ModeratorLastName{i}',
        email=f'moderator{i}@example.com',
        position='Warehouse Supervisor',
        hire_date=generate_random_date(date(2005, 1, 1), date.today()),
        phone_number=f'555-020{i}',
        address=f'Moderator {i} Address',
        password='defaultpassword',
        user_role='moderator'
    )

print("Users and employees created successfully.")
