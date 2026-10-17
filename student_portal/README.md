# Student Management System

## Project Overview
The Student Management System is a web application built using Python and Django to manage student records through a browser.

## Features
- Add new student records
- View saved student details
- Search by name, course, or email
- Edit existing records
- Delete student records
- Basic input validation for required fields and CGPA

Each student record contains a name, email, course, and CGPA. Email addresses must be unique, and CGPA must be between 0 and 10.

## Technologies Used
- Python
- Django
- SQLite
- HTML and CSS
- Git and GitHub

## Project Structure
- `config/` — Django project settings and main URL configuration
- `student_portal/` — student model, views, URLs, and templates
- `manage.py` — Django management utility

## How to Run Locally
1. Open the project folder in a terminal.
2. Activate the virtual environment.
3. Run database migrations:
   `python manage.py migrate`
4. Check the project:
   `python manage.py check`
5. Start the development server:
   `python manage.py runserver`
6. Open `http://127.0.0.1:8000/` in your browser.

## Testing
The main workflows—adding, viewing, searching, editing, and deleting student records—were manually checked. Django's system check returned: `System check identified no issues (0 silenced).`

## Limitations and Future Improvements
The application currently runs locally and has not been publicly deployed. Future improvements could include authentication, automated tests, pagination, and deployment.

## Repository
https://github.com/anshika1986CS/python-developer-internship