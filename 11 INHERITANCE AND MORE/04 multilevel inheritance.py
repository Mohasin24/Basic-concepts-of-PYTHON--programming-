# Multilevel Inheritance
'''
When a child class becomes a parent class for another child class
'''

class Person:
    country = "India"

    def takeBreath(self):
        print("Taking Breath")

class Employee(Person):
    company = 'Google'

    def getSalary(self):
        print(f"The salary of employee is {self.getSalary}")

    # def takeBreath(self):
        # print("I'm an employee luckily taking breath")  

class programmer (Employee):
    company = 'Fiverr'

    def getSalary(self):
        print(f"No salary to programmers")

    # def takeBreath(self):
        # print("I'm programmer breathing +++")  

p = Person()
e = Employee()
pr = programmer()

pr.getSalary()

print(pr.company)
print('******')

pr.takeBreath()
print(pr.company)
print(pr.country)
print('******')



