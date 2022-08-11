#Que :- Replace the double spaces from problem 3 with a single space.

st = "This is str with double  spaces."
# doubleSpaces = st.find("  ")
st = st.replace("  ",' ')
st = st.replace("double",'single')
print(st)