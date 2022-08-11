# Object oriented programming is focuses on using reusable code i.e it implements DRY principle

# Class :-A class is blueprint for creating object
# Syntax:

class Employee :  ['class name is written in pascal case i.e. first letter capital']
    methods and variables


#    PascalCase
#    EmployeeName ---> PascalCase

#    camelCase
#    isNumeric, isFloatOrInt ---> camelCase

    
#Object :-
    '''
    An object is an instantiation of a class. When class
    is defined, a template (info) is defined. Memory 
    is allocated only after object instantiation.
    '''  

    '''
    object of a given class can invoke the methods 
    available to it without revealing the implementation
    details to the user. i.e. Abstraction and encapsulation
    '''
#Modelling a problem in OOP's:-
    '''
    we identify the following in our problem
    Noun ===> Class ===> Employee
    Adjective ===> Attributes ===> name,age,salary
    Verb ===> Methods ===> getSalary(), increment()
    '''