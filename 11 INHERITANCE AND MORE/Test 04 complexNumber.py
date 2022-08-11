# (a+bi)(c+di) = (ac-bd) + (ad+bc)i

class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginary+c.imaginary)

    def __mul__(self,c):
        mulReal = self.real * c.real- self.imaginary * c.imaginary

        mulImaginary = self.real * c.imaginary + self.imaginary * c.real

        return Complex(mulReal,mulImaginary)    

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(3,2)
c2 = Complex(1,7) 
print(c1+c2)
print(c1*c2)