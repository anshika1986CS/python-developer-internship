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

    def test_search_by_course(self):
        response = self.client.get(reverse("home"), {"q": "CSE"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul Sharma")

    def test_search_by_email(self):
        response = self.client.get(
            reverse("home"), {"q": "rahul.test@example.com"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul Sharma")

    def test_search_is_case_insensitive(self):
        response = self.client.get(reverse("home"), {"q": "rahul"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul Sharma")

    def test_search_with_no_matches(self):
        response = self.client.get(
            reverse("home"), {"q": "NoSuchStudent123"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Rahul Sharma")

    def test_blank_name_is_rejected(self):
        response = self.client.post(
            reverse("add_student"),
            {
                "name": "   ",
                "email": "blank.name@example.com",
                "course": "BTech CSE",
                "cgpa": "8.0",
            }
        )
        self.assertContains(response, "Enter valid details")
        self.assertFalse(
            Student.objects.filter(
                email="blank.name@example.com"
            ).exists()
        )

    def test_cgpa_zero_is_accepted(self):
        response = self.client.post(
            reverse("add_student"),
            {
                "name": "Zero CGPA",
                "email": "zero.cgpa@example.com",
                "course": "BTech CSE",
                "cgpa": "0",
            }
        )
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(
            Student.objects.filter(
                email="zero.cgpa@example.com", cgpa=0
            ).exists()
        )

    def test_cgpa_ten_is_accepted(self):
        response = self.client.post(
            reverse("add_student"),
            {
                "name": "Maximum CGPA",
                "email": "max.cgpa@example.com",
                "course": "BTech CSE",
                "cgpa": "10",
            }
        )
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(
            Student.objects.filter(
                email="max.cgpa@example.com", cgpa=10
            ).exists()
        )

    def test_non_finite_cgpa_is_rejected(self):
        for value in ("nan", "inf", "-inf"):
            with self.subTest(cgpa=value):
                email = f"invalid-{value.replace('-', 'minus')}-cgpa@example.com"
                response = self.client.post(
                    reverse("add_student"),
                    {
                        "name": "Invalid CGPA",
                        "email": email,
                        "course": "BTech CSE",
                        "cgpa": value,
                    }
                )
                self.assertContains(response, "Enter valid details")
                self.assertFalse(
                    Student.objects.filter(email=email).exists()
                )

    def test_edit_with_duplicate_email_is_rejected(self):
        another = Student.objects.create(
            name="Priya Verma",
            email="priya.test@example.com",
            course="BTech IT",
            cgpa=9.0,
        )
        response = self.client.post(
            reverse("edit_student", args=[another.pk]),
            {
                "name": "Priya Verma",
                "email": self.student.email,
                "course": "BTech IT",
                "cgpa": "9.0",
            }
        )
        self.assertEqual(response.status_code, 200)
        another.refresh_from_db()
        self.assertEqual(another.email, "priya.test@example.com")