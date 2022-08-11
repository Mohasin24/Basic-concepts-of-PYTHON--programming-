#Que :- Can you change values in a list which is inside the set?

s = {8, 7, 12, 'Mohasin',[1,2]}
print(s)

'''we can not store list inside a set only tupples can be stored
  inside a set also set are unhashable i.e. 
 we can not change values inside set 
 if there is tupple then also we cannot change'''

 # Sets can only have tuppels inside it because tupples are immutable
 # Set's cannot contain list or dictionaries inside it because both are mutable