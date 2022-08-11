class vector:
    def __init__(self,i,j,k):
        self.i=i   
        self.j=j   
        self.k=k   

    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")

v1 = vector(7,8,10)        
print(v1)

class vector2 :
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"    

v2 = vector2([7,8,10])
print(v2)        