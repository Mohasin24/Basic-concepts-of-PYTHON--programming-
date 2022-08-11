# Que : Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from the user.

s1 = int(input('Enter s1 subjects marks: \n'))
s2 = int(input('Enter s2 subjects marks: \n'))
s3 = int(input('Enter s3 subjects marks: \n'))

#marks out of 100

if (s1<33 or s2<33 or s3<33):
    print('Your fail because you have less than 33% in one of the subject')
elif((s1+s2+s3)/3 < 40):
    print('Your fail because you have less than 40% in total')    
else:
    print('Congratulation your Passed')


    