n=input('Enter your chain')

n.lower()
lenght=len(n)
for i in n:
    if (i!='a' or i!='c' or i!='t' or i!='g'):
        n=n.replace(i,'')
    else:
        a = n.count('a')
        c= n.count('c')
        g= n.count('g')
        t = n.count('t')
lenght=len(n)
print(lenght, a, c, t, g)