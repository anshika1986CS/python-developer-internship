# Task 2 - Core Python Concepts

# 1. Variables and Data Types
name = "Anshika"
age = 21
cgpa = 8.5
is_student = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)


# 2. Conditional Statements
if cgpa >= 8:
    print("Good academic performance")
else:
    print("Need improvement")


# 3. Loops
print("\nNumbers from 1 to 5:")

for i in range(1, 6):
    print(i)


# 4. Function
def greet(student_name):
    return f"Hello, {student_name}!"


print(greet(name))

# 5. Lists
students = ["Aman", "Riya", "Rahul", "Anshika"]

print("\nStudents:")
for student in students:
    print(student)


# 6. Dictionary
student = {
    "name": "Anshika",
    "age": 21,
    "cgpa": 8.5
}

print("\nStudent Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("CGPA:", student["cgpa"])


# 7. Tuple
subjects = ("Python", "OS", "DBMS")

print("\nSubjects:", subjects)


# 8. Exception Handling
try:
    marks = int(input("\nEnter marks: "))
    print("Marks entered:", marks)

except ValueError:
    print("Please enter a valid number.")

# 9. Object-Oriented Programming (OOP)

class Student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_details(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("CGPA:", self.cgpa)

    def is_eligible(self):
        return self.cgpa >= 7.0


# Creating objects
student1 = Student("Anshika", 21, 8.5)
student2 = Student("Rahul", 20, 7.2)

student1.display_details()
print("Eligible:", student1.is_eligible())

student2.display_details()
print("Eligible:", student2.is_eligible())

# 10. Inheritance

class GraduateStudent(Student):
    def __init__(self, name, age, cgpa, specialization):
        super().__init__(name, age, cgpa)
        self.specialization = specialization

    def display_details(self):
        super().display_details()
        print("Specialization:", self.specialization)


student3 = GraduateStudent("Priya", 22, 8.8, "Computer Science")

print("\nGraduate Student:")
student3.display_details()

# 11. Encapsulation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Anshika", 5000)

account.deposit(1500)

print("\nBank Account:")
print("Owner:", account.owner)
print("Balance:", account.get_balance())

# 12. Abstraction

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key or button.")


car = Car()

print("\nAbstraction:")
car.start()

# 13. File Handling

with open("student.txt", "w") as file:
    file.write("Anshika - Computer Science - CGPA 8.5")

with open("student.txt", "r") as file:
    data = file.read()

print("\nFile Content:")
print(data)