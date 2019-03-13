from Seq import Seq

i='/seq?msg=catgaaa&chk=on&operation=count&base=A'
print(i.split('&'))
print(i.split('&')[0].split('=')[1])
seq = Seq(i)

count= {'len':seq.len(), 'base=A':seq.count('A'),
        'base=C':seq.count('C'), 'base=T':seq.count('T'), 'base=G':seq.count('G')}


perc= {'len':seq.len(), 'base=A':seq.perc('A'),'base=C':seq.perc('C'),'base=T':seq.perc('T'),
       'base=G':seq.perc('G')}

ops = {'count':count, 'perc':perc}

print(type(len('ahnfuhgdhbibg')))