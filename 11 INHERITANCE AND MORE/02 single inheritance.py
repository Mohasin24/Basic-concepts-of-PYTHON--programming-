#Single inheritance :
'''
single inheritance occurs when child class inherits only a single parent class
'''

class Employee:
    company = 'Google'

    def showDetails(self):
        print('This is an employee')

class Programmer(Employee):
    language = 'Python'
    # company = 'Youtube'

    def getLanguage(self):
        print(f"The language is {self.language}.")

    def showDetails(self):
        print('This is an programmer')        

e = Employee()
p = Programmer()       

e.showDetails()
# print(e.company)
print(p.company)
p.showDetails()


