# List methods
l1 = [1, 3, 8, 2, 5, 7, 4, 6]

# List sort > will sort the list in order
l1.sort()
print(l1)
print("\n")

# List reversed > will sort list in reversed order
l1.reverse()
print(l1)
print("\n")

# Append > adds a character at the end of the list [it is IMP]
# it will add the character at the end of the list and will not replace any character
l1.append(45)
print(l1)
print("\n")

# Insert

l1.insert(0,544) #inserts 544 at index 0 but did not replace the element at the 0th index it changes its index
print(l1)
print("\n")

#Pop > delete element at the specified index
l2 = [5,10,15,20,25,30,35,40]
l2.pop(2)
print(l2)
print("\n")

#Remove > will remove the value

l2.remove(30)
print(l2)
print("\n")

# List length:

print(len(l2))
print("\n")
