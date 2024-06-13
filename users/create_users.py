# users/create_users.py

import os
import django
from django.test import Client
from django.urls import reverse
from datetime import date, timedelta
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouseApp.settings')
django.setup()

from users.models import CustomUser

def generate_random_date(start, end):
    """Generate a random date between start and end."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def create_user(client, username, first_name, last_name, email, position, hire_date, phone_number, address, password, user_role):
    """Create a user by sending a POST request to the registration view and setting user role."""
    registration_url = reverse('user_registration')  # URL of the registration view
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
    response = client.post(registration_url, form_data)
    if response.status_code == 302:  # Check if redirect (indicating success)
        # Fetch the created user and update the user_role
        user = CustomUser.objects.get(username=username)
        user.user_role = user_role
        user.save()
        print(f'Successfully created {user_role}: {username}')
    else:
        print(f'Failed to create {user_role}: {username}', response.content)

def main():
    client = Client()

    # Create 10 employees
    for i in range(1, 11):
        create_user(
            client=client,
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

    # Create 5 moderators
    for i in range(1, 6):
        create_user(
            client=client,
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

if __name__ == '__main__':
    main()
