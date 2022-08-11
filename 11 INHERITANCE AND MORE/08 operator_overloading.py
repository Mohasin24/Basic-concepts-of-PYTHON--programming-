# operator overloading :
'''
Operator in python can be overloaded using dunder methods.
These methods are called when a given operator is used on the objects.
'''

#Operators in python can be overloaded using the following method
'''
n1 + n2 --> n1__add__n2
n1 - n2 --> n1__sub__n2
n1 * n2 --> n1__mul__n2
n1 / n2 --> n1__truediv__n2
n1 // n2 --> n1__floordiv__n2 
'''


class Number :
    def __init__(self,num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")   
        return self.num + num2.num

    def __sub__(self,num2):
       print("Lets substract")
       return self.num - num2.num      

    def __mul__(self, num2):
        print("Lets multiply")
        return (self.num * num2.num)

    def __truediv__(self,num2):
        print("Lets divide")
        return (self.num/num2.num) 

    def __floordiv__(self,num2):
        print('Lets floor divide')
        return (self.num//num2.num)       

n1 = Number(6)
n2 = Number(4)
sum = n1+n2  

mul = n1*n2

sub = n1-n2

truediv = n1 / n2

floordiv = n1 // n2

print(sum)
print('------') 
print(sub) 
print('------') 
print(mul) 
print('------') 
print(truediv)     
print('------')
print(floordiv)  
print('------')  