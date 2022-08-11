# Static Method :
'''
Sometimes we need a function that doesn't use the 'self' parameter. 
We can define a static method
'''
class Employee :
    company = 'Google'
    def getSalary(self):
        print(f'Salary is {self.salary}') # here 'self' is mohasin  

    @staticmethod    #decorator to mark greet as a static method
    def greet():
        print('Good Morning, Sir!')

    @staticmethod
    def time():
        print('Time is 9 AM')    

mohasin = Employee()

mohasin.salary = 100000

mohasin.getSalary()      # Employee.getSalary(mohasin) 

mohasin.greet() #Employee.greet()

mohasin.time()

