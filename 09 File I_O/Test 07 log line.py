file = True
i = 1 #line counter
with open('sample log.txt', 'r') as f:
    while file :        
        file = f.readline()           
        if 'python' in file.lower(): 
          print(file,end='')          
          print('Yes, Python is present & the line no. is:-',i)
        i +=1      