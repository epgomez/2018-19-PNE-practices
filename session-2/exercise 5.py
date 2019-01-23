with open('filename', 'r') as n:

    n= n.
    n= n.replace('\n','')
    n = n.lower()

    for i in n:
        if not (i=='a' or i=='c' or i=='t' or i=='g'):
            n=n.replace(i,'')
    a = n.count('a')
    c= n.count('c')
    g= n.count('g')
    t = n.count('t')
    lenght=len(n)
    print('\nTotal lenght: ',lenght,'\nA: ',a,'\nC: ',c,'\nT: ', t,'\nG: ', g)