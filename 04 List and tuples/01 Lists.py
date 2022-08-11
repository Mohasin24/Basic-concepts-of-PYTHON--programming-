#Lists :- lists are mutable
# python lists are conatiners to store set of values of any data type,we use [] brackets to write lists
from matplotlib.pyplot import pink


a = [10,20,30,40,50] 

#Lists indexing > you can index items of lists just like str

print(a[2]) #output - 30

#also you can change the list elements

a[0] = 100 #10 will be replaced by 100

print(a)

# we can create list with items of different datatypes

c = [25, 'mohasin', True, 3.3 , None]

print(c)
print(type(c))



#List slicing

friends = ['mohasin', 'harry', 'berlin', 'tokyo', 'denver', 'professor']

print(friends[0::2],"\n")

#reverse order

print("\t*****\n",friends[::-2])

