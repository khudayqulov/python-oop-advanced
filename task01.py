"""Task 01 — Student Management: class and instance attributes."""


class Student:
    university = "Tashkent University"

    def __init__(self, name, age, student_id):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.name = name.strip()
        self.age = age
        self.student_id = student_id

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"

    def is_adult(self):
        return self.age >= 18


def demo():
    students = [
        Student("Ali", 22, 101),
        Student("Vali", 17, 102),
        Student("Sardor", 18, 103),
    ]
    for student in students:
        print(student.get_info(), "| Adult:", student.is_adult())

    # Class attribute versus an instance attribute of the same name.
    Student.university = "New University"
    students[0].university = "My University"
    print("First:", students[0].university)
    print("Second:", students[1].university)
    Student.university = "Tashkent University"


if __name__ == "__main__":
    demo()
