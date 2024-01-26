
class Employee:
    count = 0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1
    def averageSalary(self):
        avg = self.salary / Employee.count
        return avg

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

e1 = Employee("John", "Smith", 48000, "IT")
e2 = Employee("David", "Jones", 45000, "HR")
e3 = FulltimeEmployee("Sam", "Williams", 60000, "Marketing")

print(e1.averageSalary())
print(e2.averageSalary())
print(e3.averageSalary())