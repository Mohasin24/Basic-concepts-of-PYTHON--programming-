with open('donkey.txt', 'r') as f:
    con = f.read()
con = con.lower()    
con = con.replace('donkey', '#####')


with open('donkey.txt', 'w') as f:
    f.write(con)