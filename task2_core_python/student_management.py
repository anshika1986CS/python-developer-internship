import json


class Student:
    def __init__(self, name, age, course, cgpa):
        self.name = name
        self.age = age
        self.course = course
        self.cgpa = cgpa

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "cgpa": self.cgpa
        }


class StudentManager:

    def __init__(self, filename="students.json"):
        self.filename = filename

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, students):
        with open(self.filename, "w") as file:
            json.dump(students, file, indent=4)

    def add_student(self, student):
        students = self.load_students()
        students.append(student.to_dict())
        self.save_students(students)

    def display_students(self):
        students = self.load_students()

        if not students:
            print("No students found.")
            return

        print("\nStudent Records:")

        for student in students:
            print("--------------------")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("CGPA:", student["cgpa"])

    def search_student(self, name):
        students = self.load_students()

        for student in students:
            if student["name"].lower() == name.lower():
                print("\nStudent Found:")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("CGPA:", student["cgpa"])
                return

        print("Student not found.")


def main():

    manager = StudentManager()

    while True:

        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            cgpa = float(input("Enter CGPA: "))

            student = Student(name, age, course, cgpa)

            manager.add_student(student)

            print("Student added successfully.")

        elif choice == "2":

            manager.display_students()

        elif choice == "3":

            name = input("Enter student name: ")
            manager.search_student(name)

        elif choice == "4":

            print("Thank you for using Student Management System.")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()