# Instance attribute:
'''
An attribute that belongs to the instance(object)
'''
#Example:

class Employee :
    company = 'Google' #Specific to each class
    salary = 100     #class attribute

Mohasin = Employee() #object instantiation
Rajni = Employee()  

#creating instance attribute:
Mohasin.salary = 200
Rajni.salary = 300

print(Mohasin.company)
print(Rajni.company) 

Employee.company = 'YouTube' #changing class attribute
print(Mohasin.company) 
print(Rajni.company) 

print (Mohasin.salary)
print(Rajni.salary)

#Note :> Instance attribute take preference over class attributes
# during assignments & retrival