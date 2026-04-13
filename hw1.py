class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)


emp = Employee("Ali", 25, 5000)

emp.display_info()
emp.display_salary()