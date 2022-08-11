#Set Methods

a = set()

# 01_Add method : used to add elements in an empty set

a.add(5)
a.add(7)
a.add(2)
a.add(2) #adding a repitative element does not change the set

''' a.add[2,5,8] We cannot add a list and dict into an empty set because 
it is not hashable i.e. we can change list/dict elements 
but set are not changeable '''

a.add((4,8,9)) #we can add tupple into set because tupple and sets both are non changeable

print(a,"\n")
 
# 02_length method : it will give the length of sets or no. of items in a set

print("The length of set :-\n",len(a))

# # 03_Remove : removes desired item from set
# print("\nRemove items from set:-\n")
# a.remove((4,8,9)) #also we cannot remove single item from a tupple we have to remove whole tupple

# a.remove(2)
# print(a)

# 04_pop method : it will remove any random item from a set
# print("\nPop method:-\n")
# a.pop()
# print(a)

# 05_Clear : this will empties the set

# a.clear()
# print(a)

# 06_Union : returns the set with combining sets

a=a.union({1,6,10})
print(a) #also print(a1|a2) i.e a1 union a2

# 07_intersection : returns the set with same elements

print(a.intersection({5,7,9}))
print("\n----****-----\n")

#also print(a1&a2) i.e. a1 intersecton a2

#08_Difference:
'''
Difference of A and B ,(A-B) is a set of elements that are only in A but not in B.
Similarly, (B-A) is a set of elements that are only in B but not in A 
'''
a1= {1,2,3}
a2={4,5,6}
print(a2-a1)

