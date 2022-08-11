# -__init__ constructor:-
'''
__init__ is a special method which is first run as soon as is created
'''
'''
It takes self argument and can also take further arguments
'''
class Employee :
    company = 'Google'

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print('Employee is created!')

    def getDetails(self):
        print(f'The name of the employee is {self.name}')
        print(f'The salary of the employee is {self.salary}')
        print(f'The subunit of the employee is {self.subunit}')

    def getSalary(self):
        print(f'Salary is {self.salary}') # here 'self' is mohasin  

    @staticmethod    #decorator to mark greet as a static method
    def greet():
        print('Good Morning, Sir!')

    @staticmethod
    def time():
        print('Time is 9 AM')    

harry = Employee('Mohasin',100,'YouTube') 

#harry = Employee()# ---> This throws an error (missing 3 required positional arguments: 'name', 'salary', and 'subunit')

harry.getDetails()