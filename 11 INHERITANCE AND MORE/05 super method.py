#super method :-
'''
super method is used to access the methods of a super class in the derived class

        super().__init__() : this calls the constructor of the base class
'''

class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person")

    def takeBreath(self):
        print("Taking Breath")

class Employee(Person):
    company = 'Google'

    def __init__(self):
        super().__init__()
        print("Initializing Employee")

   
    def getSalary(self):
        print(f"The salary of employee is {self.getSalary}")

    def takeBreath(self):
        super().takeBreath()  
        print("I'm an employee luckily taking breath")  

class programmer (Employee):
    company = 'Fiverr'

    def __init__(self):
        super().__init__()
        print("Initializing Programmer")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()  #first runs parents takeBreath
        print("I'm programmer breathing +++")  

# p = Person()
# p.takeBreath()
# print('--------')

# e = Employee()
# e.takeBreath()
# print('--------')

pr = programmer()
# pr.__init__()
pr.takeBreath()