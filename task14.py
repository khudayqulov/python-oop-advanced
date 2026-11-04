"""Task 14 — University management with courses, enrollments and GPA."""


class Person:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        self.name = name.strip()


class Grade:
    def __init__(self, points):
        if (isinstance(points, bool)
                or not isinstance(points, (int, float))
                or not 0 <= points <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.points = points

    def gpa_points(self):
        if self.points >= 90:
            return 4.0
        if self.points >= 80:
            return 3.0
        if self.points >= 70:
            return 2.0
        if self.points >= 60:
            return 1.0
        return 0.0


class Course:
    def __init__(self, name, credits):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Course name cannot be empty")
        if isinstance(credits, bool) or not isinstance(credits, int) or credits <= 0:
            raise ValueError("Credits must be a positive integer")
        self.name = name
        self.credits = credits
        self.teacher = None
        self.enrollments = []


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None


class Student(Person):
    student_count = 0

    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.enrollments = []
        Student.student_count += 1

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise TypeError("Student data must be a dictionary")
        return cls(data["name"], data["student_id"])

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    def enroll(self, course):
        if not isinstance(course, Course):
            raise TypeError("Expected a Course")
        if any(enrollment.course is course for enrollment in self.enrollments):
            raise ValueError("Student already enrolled in this course")
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)
        return enrollment

    def get_gpa(self):
        graded = [e for e in self.enrollments if e.grade is not None]
        credits = sum(e.course.credits for e in graded)
        if credits == 0:
            return 0.0
        weighted = sum(
            e.grade.gpa_points() * e.course.credits for e in graded
        )
        return weighted / credits


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def assign_to_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("Expected a Course")
        if course.teacher is not None and course.teacher is not self:
            raise ValueError("Course already has another teacher")
        if course not in self.courses:
            self.courses.append(course)
        course.teacher = self

    def grade_student(self, student, course, points):
        if course.teacher is not self:
            raise ValueError("Teacher is not assigned to this course")
        for enrollment in student.enrollments:
            if enrollment.course is course:
                enrollment.grade = Grade(points)
                return enrollment.grade
        raise ValueError("Student is not enrolled in this course")


class Admin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.students = []
        self.teachers = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Expected a Student")
        if student in self.students:
            raise ValueError("Student is already registered")
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Expected a Teacher")
        if teacher in self.teachers:
            raise ValueError("Teacher is already registered")
        self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        self.teachers.remove(teacher)


def demo():
    students = [
        Student.from_dict({"name": "Ali", "student_id": 1}),
        Student("Vali", 2),
        Student("Sardor", 3),
    ]
    admin = Admin("Dean")
    teacher = Teacher("Professor")
    python_course = Course("Python", 4)
    math_course = Course("Math", 2)
    admin.add_teacher(teacher)
    teacher.assign_to_course(python_course)
    teacher.assign_to_course(math_course)

    for student, points in zip(students, [95, 85, 75]):
        admin.add_student(student)
        student.enroll(python_course)
        teacher.grade_student(student, python_course, points)
        print(student.name, "GPA:", student.get_gpa())

    students[0].enroll(math_course)
    teacher.grade_student(students[0], math_course, 70)
    print("Ali weighted GPA:", students[0].get_gpa())


if __name__ == "__main__":
    demo()
