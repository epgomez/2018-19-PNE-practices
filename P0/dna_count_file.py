with open('dna.txt', 'r') as n:
    lenght = 0
    a, c, t, g = 0, 0, 0, 0
    for line in n:
        str(line)
        line = line.lower()
        for i in line:
            if not (i == 'a' or i == 'c' or i == 't' or i == 'g'):
                line = line.replace(i, '')
        a += line.count('a')
        c += line.count('c')
        g += line.count('g')
        t += line.count('t')
        lenght += len(line)
    print('\nTotal lenght: ', lenght, '\nA: ', a, '\nC: ', c, '\nT: ', t, '\nG: ', g)
