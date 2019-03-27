n: str=input("""Enter your chain (If you enter a letter that doesn\'t represent a base,
 it will be deleted and it will not be considered for the total lenght): """)
n = n.lower()
lenght=len(n)
for i in n:
    if not (i=='a' or i=='c' or i=='t' or i=='g'):
        n=n.replace(i,'')
a = n.count('a')
c= n.count('c')
g= n.count('g')
t = n.count('t')
lenght=len(n)
print('Total lenght: ',lenght,'\nA: ',a,'\nC: ',c,'\nT: ', t,'\nG: ', g)