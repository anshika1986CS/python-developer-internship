# Student Management System

## Project Overview
A web-based Student Management System built using Python and Django. It helps users manage student records through a simple browser interface.

## Features
- Add student records
- View all student records
- Search by name, course, or email
- Edit existing records
- Delete student records
- Validate student details and CGPA
- Store records in a database using Django ORM

## Technologies Used
- Python
- Django
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure
- `models.py` — Defines the Student database model.
- `views.py` — Handles application logic.
- `urls.py` — Defines application routes.
- `templates/student_portal/` — Contains the HTML pages.
- `migrations/` — Contains database migration files.

## Run Locally
1. Install Python and Django in your environment.
2. Open a terminal in the project root.
3. Run database migrations:

   `python manage.py migrate`

4. Start the development server:

   `python manage.py runserver`

5. Open `http://127.0.0.1:8000/` in your browser.

## Note
This project currently runs locally and has not been deployed as a public website.

## Future Improvements
- User authentication
- Automated tests
- Pagination
- Public deployment
