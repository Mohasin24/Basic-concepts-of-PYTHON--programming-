# Class Attribute:
'''
An attribute that belongs to the class rather than a particular object.
'''

#Example:

class Employee :
    company = 'Google' #Specific to each class

Mohasin = Employee() #object instantiation
Rajni = Employee() 
print(Mohasin.company)
print(Rajni.company) 

Mohasin.company = 'YouTube' #changing class attribute
Employee.company = 'Adobe' 
print(Mohasin.company) 
print(Rajni.company) 