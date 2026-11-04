"""Task 03 — Classmethod and employee counter."""


class Employee:
    employee_count = 0

    def __init__(self, name, position, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1

    def get_info(self):
        return f"{self.name} | {self.position} | {self.salary}"

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


def demo():
    employees = [
        Employee("Ali", "Developer", 5000),
        Employee("Vali", "Designer", 4000),
        Employee("Sardor", "Manager", 7000),
    ]
    for employee in employees:
        print(employee.get_info())
    print("Objects created:", Employee.get_employee_count())
    

if __name__ == "__main__":
    demo()
