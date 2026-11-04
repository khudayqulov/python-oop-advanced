"""Task 07 — Employee inheritance, super() and overriding."""


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def write_code(self):
        return f"{self.name} writes {self.programming_language} code"

    def get_info(self):
        return f"{super().get_info()}, Language: {self.programming_language}"


class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self):
        return f"{self.name} creates designs using {self.design_tool}"

    def get_info(self):
        return f"{super().get_info()}, Design tool: {self.design_tool}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        if isinstance(team_size, bool) or not isinstance(team_size, int) or team_size < 0:
            raise ValueError("Team size must be a non-negative integer")
        self.team_size = team_size

    def manage_team(self):
        return f"{self.name} manages {self.team_size} employees"

    def get_info(self):
        return f"{super().get_info()}, Team size: {self.team_size}"


def demo():
    employees = [
        Developer("Ali", 6000, "Python"),
        Designer("Vali", 5000, "Figma"),
        Manager("Sardor", 8000, 5),
    ]
    for employee in employees:
        print(employee.get_info())
    print(employees[0].write_code())
    print(employees[1].create_design())
    print(employees[2].manage_team())


if __name__ == "__main__":
    demo()
