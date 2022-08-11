f= open('poem.txt', 'r')
t = f.read()
if 'twinkle' in t:
    print('Twinkle is present in the given poem!')
else:
    print('Twinkle is not present in the given poem')
f.close()
