# Multilevel inheritance
class Animals:
    type = 'Mammel'

class Pets(Animals):
    colour = 'White'

class Dog(Pets):
    
    @staticmethod
    def bark():         #here we are not using 'self' because it is not using any class attribute or instance attribute
        print('Bow Bow!')

d = Dog()
d.bark()        
print(d.colour)
print(d.type)