from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from django.db import IntegrityError, transaction


def home(request):
    query = request.GET.get("q", "")
    students = Student.objects.all().order_by("name")

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(course__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, "student_portal/home.html", {
        "students": students,
        "query": query,
    })



def add_student(request):
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        course = request.POST.get("course", "").strip()
        cgpa_text = request.POST.get("cgpa", "").strip()

        try:
            cgpa = float(cgpa_text)

            if not name or not email or not course:
                raise ValueError

            if not 0 <= cgpa <= 10:
                raise ValueError

            try:
                with transaction.atomic():
                    Student.objects.create(
                        name=name,
                        email=email,
                        course=course,
                        cgpa=cgpa
                    )

            except IntegrityError:
                error = "Could not save student. Check that the email is unique."

            else:
                return redirect("home")

        except ValueError:
            error = "Enter valid details. CGPA must be between 0 and 10."

    return render(
        request,
        "student_portal/form.html",
        {"student": None, "error": error}
    )



def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        course = request.POST.get("course", "").strip()
        cgpa_text = request.POST.get("cgpa", "").strip()

        try:
            cgpa = float(cgpa_text)
            if not name or not email or not course or not 0 <= cgpa <= 10:
                raise ValueError
            student.name = name
            student.email = email
            student.course = course
            student.cgpa = cgpa
            student.save()
            return redirect("home")
        except ValueError:
            error = "Enter valid details. CGPA must be between 0 and 10."
        except Exception:
            error = "Could not update student. Check that the email is unique."

    return render(request, "student_portal/form.html", {
        "student": student, "error": error
    })


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "POST":
        student.delete()

    return redirect("home")