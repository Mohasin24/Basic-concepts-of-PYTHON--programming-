f = open('sample.txt' , 'r')

# read first line
data = f.readline()  #readline function only reads 1 line
print(data,end='')

# read second line
data = f.readline()  #readline function only reads 1 line
print(data)
f.close()