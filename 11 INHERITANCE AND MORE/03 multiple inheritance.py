#Multiple inheritance :
'''
Multiple inheritance occurs when the child class inherits from more than one parent class
'''

class Employee:
    company = 'Visa'
    eCode = 120
    
    def getName(self):
        name = 'Employee'
        self.name=name

class Freelancer :
    company = 'Fiverr'
    level = 1

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee,Freelancer):
    name = 'Mohasin'   

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company) #we have derived employee class first in programmer
print(p.eCode)
print(p.name)