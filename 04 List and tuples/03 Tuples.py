#Tuples > we cannot change data in tuples it is fixed i.e. it is immutable
# Tuples are written in round brackets

t = (35,20,58,) # comma is must after every element even it contains 1 element
print("\n",t)
# t[0] = 34 we can not change values in tuples they are fixed
print(t[2],"\n") # we can call index in tuple

#EMpty tuple

t1 = ()
print(type(t1))
print(t1,"\n")

#Tuple with only one element needs a comma
t2 = (2) #this is a wrong way to declare a tuple it will get executed as a integer not a tuple

print(t2)
print(type(t2),"\n")

t3 = (2,)
print(t3)
print(type(t3))