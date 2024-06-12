# WarehouseAttendanceApp

WarehouseAttendanceApp is a Django-based web application for managing and tracking employee attendance.

## Features

- Manage employee roles and permissions.
- Track employee attendance.
- Implement custom user roles: Superuser, Moderator, and Employee.

## Setup and Installation

To set up and run the project locally:

1. **Clone the repository** to your local machine.
2. **Create and activate a virtual environment** (optional but recommended).
3. **Install the required dependencies** listed in `requirements.txt`.
4. **Configure your database** settings in `settings.py`.
5. **Apply database migrations** to set up the initial database schema.
6. **Create a superuser** to access the admin panel.
7. **Run the development server** and access the application via your web browser.

## Running the Application

1. Start the Django development server.
2. Access the application through the provided local URL (usually `http://127.0.0.1:8000/`).

## Custom User Model

The project uses a custom user model to accommodate different user roles (Superuser, Moderator, Employee). 

## Troubleshooting

If you encounter any issues during setup or running the application:

1. Ensure all dependencies are installed correctly.
2. Verify database configurations and apply migrations as needed.
3. Check for any conflicting migrations or database entries and resolve them.

For more detailed guidance or troubleshooting, consult the [Django documentation](https://docs.djangoproject.com/).

## Contributions

Feel free to contribute by opening issues, suggesting features, or submitting pull requests. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
