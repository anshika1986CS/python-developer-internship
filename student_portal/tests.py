
from django.test import TestCase
from django.urls import reverse
from .models import Student


class StudentManagementTests(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            name="Rahul Sharma",
            email="rahul.test@example.com",
            course="BTech CSE",
            cgpa=8.5
        )

    def test_student_record_is_saved(self):
        student = Student.objects.get(
            email="rahul.test@example.com"
        )
        self.assertEqual(student.name, "Rahul Sharma")
        self.assertEqual(student.cgpa, 8.5)

    def test_home_page_displays_student(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul Sharma")

    def test_search_by_name(self):
        response = self.client.get(
            reverse("home"), {"q": "Rahul"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul Sharma")

    def test_add_student(self):
        response = self.client.post(
            reverse("add_student"),
            {
                "name": "Priya Verma",
                "email": "priya.test@example.com",
                "course": "BTech IT",
                "cgpa": "9.0",
            }
        )
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(
            Student.objects.filter(
                email="priya.test@example.com"
            ).exists()
        )

    def test_edit_student(self):
        response = self.client.post(
            reverse("edit_student", args=[self.student.pk]),
            {
                "name": "Rahul Sharma",
                "email": "rahul.test@example.com",
                "course": "BTech CSE",
                "cgpa": "9.0",
            }
        )
        self.assertRedirects(response, reverse("home"))
        self.student.refresh_from_db()
        self.assertEqual(self.student.cgpa, 9.0)

    def test_delete_student(self):
        response = self.client.post(
            reverse("delete_student", args=[self.student.pk])
        )
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(
            Student.objects.filter(pk=self.student.pk).exists()
        )
   
    def test_invalid_cgpa_is_rejected(self):
        response = self.client.post(
            reverse("add_student"),
            {
                "name": "Test Student",
                "email": "invalid.cgpa@example.com",
                "course": "BTech CSE",
                "cgpa": "12",
            }
        )
        self.assertContains(
            response,
            "CGPA must be between 0 and 10."
        )
        self.assertFalse(
            Student.objects.filter(
                email="invalid.cgpa@example.com"
            ).exists()
        )

    def test_duplicate_email_is_rejected(self):
        response = self.client.post(
            reverse("add_student"),
            {
                "name": "Another Student",
                "email": "rahul.test@example.com",
                "course": "BTech IT",
                "cgpa": "8.0",
            }
        )
        self.assertContains(
            response,
            "Could not save student. Check that the email is unique."
        )
        self.assertEqual(
            Student.objects.filter(
                email="rahul.test@example.com"
            ).count(),
            1
        )
