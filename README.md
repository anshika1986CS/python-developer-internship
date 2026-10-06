# Python Developer Internship

This repository contains my work for the Python Developer Fresher internship, covering Python fundamentals, development environment setup, Django basics, and version control using Git and GitHub.

## Task 1 – Fundamentals and Setup

The objective of Task 1 was to understand the Python development environment, set up the required tools, learn basic project structure and conventions, and create a simple Hello World program.

### Technologies Used

- Python 3.14.2
- Django 6.1.2
- Git
- GitHub
- Visual Studio Code
- Python Virtual Environment

### Project Structure

```text
PythonDeveloperInternship/
│
├── .venv/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── hello.py
├── manage.py
├── .gitignore
└── README.md
```

### Hello World

A basic Python program was created to understand Python file execution and program structure.

```python
def main():
    print("Hello, World!")
    print("Python Developer Internship - Task 1")


if __name__ == "__main__":
    main()
```

### Django Setup

A Django project was created using:

```bash
django-admin startproject config .
```

The development server can be started with:

```bash
python manage.py runserver
```

The application runs locally at:

```text
http://127.0.0.1:8000/
```

### Git and GitHub

Git was initialized in the project directory to track source-code changes. The project was committed and pushed to GitHub using the `main` branch.

Git helps maintain the history of project changes, while GitHub provides a remote repository for storing and sharing the project.

## Learning Outcomes

Through Task 1, I gained practical experience in setting up a Python development environment, using a virtual environment, creating and running a Python program, understanding the basic structure of a Django project, running a Django development server, and using Git and GitHub for version control.

## Future Work

The upcoming tasks will build on this foundation by covering Python programming concepts, object-oriented programming, Django application development, databases and ORM, REST APIs, testing, debugging, and deployment.
