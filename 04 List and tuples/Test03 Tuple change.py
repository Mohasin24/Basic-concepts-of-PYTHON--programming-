#Que :- Check the tuple cannot be changed   
try:
    t1 = (25,24,67,78,)
    t1[2]=5

    t2 = ('mk','jd')
    t2[0] = 'kl'
except Exception as e:
    print(e)    