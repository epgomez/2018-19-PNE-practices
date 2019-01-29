with open('CPLX2.txt', 'r') as n:
    a, c, t, g = 0, 0, 0, 0
    for line in n:
        if '>' in line:
            line=''
        a += line.count('A')
        c += line.count('C')
        t += line.count('T')
        g += line.count('G')
print('A: ', a, '\nC: ', c, '\nT: ', t,'\nG: ', g)