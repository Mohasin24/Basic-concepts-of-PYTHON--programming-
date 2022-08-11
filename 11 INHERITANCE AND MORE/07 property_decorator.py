# @.getter
'''
The method name with @property decorator is called getter 
method.
'''
# @.setter
'''
we can define a function+@name.setter decorator like
below:
@name.setter
def name(self,value):
    self.ename = value 
'''



class Employee:
    company = 'HP Gas'
    salary = 4500
    salaryBonus = 500

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter 

    def totalSalary(self,val):
        self.salaryBonus = val - self.salary  

e =Employee()    
print(e.totalSalary)
e.totalSalary = 5500
print(e.salary)
print(e.salaryBonus)