# WarehouseAttendanceApp

WarehouseAttendanceApp is a powerful, Django-based web application designed to streamline employee attendance tracking using facial recognition technology.

## Table of Contents
1. [Features](#features)
2. [Demo](#demo)
3. [Getting Started](#getting-started)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Usage](#usage)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)

## Features

- 🖥️ **Real-Time Facial Recognition**: Capture and identify employees using advanced AI technology.
- 🔒 **Custom User Roles**: Manage Superuser, Moderator, and Employee roles with specific permissions.
- 📅 **Attendance Tracking**: Efficiently track employee attendance with a user-friendly interface.
- 📊 **Dashboard Overview**: Access detailed insights and summaries of attendance records.
- 📷 **Webcam Integration**: Use the built-in webcam to capture employee images for attendance marking.

## Demo

🎥 Check out a video walkthrough of the app in action here: [Working Walkthrough](/screensnaps/LinkedInPost.mp4) (Replace `#` with your video link)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **Django 3.2+**
- **pip** (Python package installer)
- **virtualenv** (for creating isolated Python environments)
- **Git** (for cloning the repository)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/WarehouseAttendanceApp.git
   cd WarehouseAttendanceApp
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv appEnv
   source appEnv/bin/activate  # On Windows use `appEnv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your database** settings in settings.py (default is SQLite, but you can switch to other databases like PostgreSQL or MySQL).

5. **Apply database migrations** to set up the initial database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** for accessing the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

### Configuration

1. **Set up environment variables** (optional):
   - Create a `.env` file in the root directory.
   - Define any environment-specific variables like `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, etc.

2. **Modify `settings.py`** to include any custom configurations or integrations you need.

3. **Static and Media Files**:
   - Collect static files if you're running in production:

     ```bash
     python manage.py collectstatic
     ```

### Running the Application

1. **Start the Django development server**:

   ```bash
   python manage.py runserver
   ```

2. **Access the application** through the provided local URL, http://127.0.0.1:8000/

### Features

- **Face Recognition Attendance**: Capture and recognize employees' faces to mark attendance.
- **Role-Based Access**: Manage different user roles such as Superuser, Moderator, and Employee.
- **Admin Dashboard**: Access and manage user roles, attendance records, and other administrative tasks via Django's admin interface.

### Custom User Model

The project uses a custom user model to support different roles (Superuser, Moderator, Employee) with distinct permissions and capabilities.

### Troubleshooting

If you encounter issues:

1. **Dependencies**: Make sure all dependencies in `requirements.txt` are installed.
2. **Database**: Verify database settings and apply migrations if needed.
3. **Migrations**: Check for and resolve any conflicting migrations or database entries.

For more detailed guidance, refer to the [Django documentation](https://docs.djangoproject.com/).

### Contributions

We welcome contributions! Feel free to open issues, suggest features, or submit pull requests.
