

# Student Management System

## Project Overview
A web application built with Python and Django to manage student records through a browser.

## Features
- Add and view student records
- Search students by name, course, or email
- Edit and delete student records
- Validate required fields and CGPA
- Prevent duplicate email addresses
- Handle database errors during record updates

Each student record contains a name, email, course, and CGPA. CGPA must be between 0 and 10, and email addresses must be unique.

## Technologies Used
- Python
- Django
- SQLite
- HTML and CSS
- Git and GitHub

## Project Structure
- `config/` — Django project settings and main URL configuration
- `student_portal/` — student model, views, URLs, templates, and tests
- `manage.py` — Django management utility

## How to Run Locally
1. Open the project folder in a terminal.
2. Activate the project's virtual environment.
3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Check the project configuration:

   ```bash
   python manage.py check
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## Testing and Quality Assurance

Automated tests cover the main student-management workflows, input validation, and error-handling scenarios.

Run the test suite using:

```bash
python manage.py test student_portal
```

**Latest test result:** 17 tests passed.

The Django system check also completed successfully with no issues:

```text
System check identified no issues (0 silenced).
```

The edit workflow uses `transaction.atomic()` and handles `IntegrityError` to manage database integrity errors during updates.

## Limitations and Future Improvements
- The application runs locally and has not been publicly deployed.
- Performance and load testing can be added in future.
- Integration testing and authentication can be expanded.
- Pagination and additional usability improvements can be introduced.

## Repository
https://github.com/anshika1986CS/python-developer-internship
