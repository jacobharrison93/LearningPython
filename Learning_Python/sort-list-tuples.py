class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return f'({self.name},{self.age},${self.salary})'
from operator import attrgetter

e1 = Employee('Carl',27,55000)
e2 = Employee('Mark',55,100000)
e3 = Employee('Sara',34,75000)

employees = [e1,e2,e3]

s_employees = sorted(employees, key = attrgetter('age'))
print(s_employees)