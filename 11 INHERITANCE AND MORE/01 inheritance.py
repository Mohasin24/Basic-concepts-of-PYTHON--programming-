#Inheritance:
'''
inheritance is a way of creating new class from existing class
'''

'''
we can use all methods and attribute of employee in programmer object
Also, we can overwrite or add new attributes and method in programmer class
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
p.getLanguage()


