#Self Parameter:
'''
Self refers to the instance(object) of the class. It is automatically passed with a 
function call from an object.
'''

class Employee :
    company = 'Google'
    salary = 500

    def getSalary(self):
        salary = self.salary  #here 'self' is mohasin  
        print(f'Salary is {salary}') 

mohasin = Employee()

# mohasin.salary = 100000

mohasin.getSalary()      # Employee.getSalary(mohasin)  