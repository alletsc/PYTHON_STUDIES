class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_rise(self, rise=5000):
        self.salary += rise
        return self.salary
