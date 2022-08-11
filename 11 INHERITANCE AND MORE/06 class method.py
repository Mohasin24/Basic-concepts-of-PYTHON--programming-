#Class Method:
'''
a class method is method which is bound to the class and not to the object of class
@classmethod decorator is used to create a class method

aisa method jo class se juda hua hai na ki object se        
'''
#syntax:
'''
@classmethod
def(cls,p1,p2):
'''
class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal
    '''
    this will change the class attribute and it is called as Dunder method
    '''

    @classmethod
    def changeSalary(cls, salary2): #now it will change the class attribute not the instance attribute
        cls.salary = salary2
        
    @classmethod
    def changeLocation(cls,loc):
        cls.location=loc    

e = Employee()   
print(e.salary)      #here e.salary is a instance attribute i.e. object attribute 
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
e.changeLocation('nagar')
print(e.location)
print(Employee.location)
