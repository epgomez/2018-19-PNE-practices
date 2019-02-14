from Seq import Seq

s1 = Seq(input('seq 1: '))
s2 = Seq(input('seq 2: '))
s3 = s1.complement()
s4 = (Seq(s3)).reverse()

seqs = [s1,s2,Seq(s3),Seq(s4)]
order = [1,2,3,4]

for elem, i in zip(seqs, order):
    print('Sequence {}: {}'.format(i,elem.strbases.upper()))
    print('Lenght of the sequence: ', elem.len())
    bases = ['A', 'C', 'T', 'G']
    for i in bases:
        print('\nNumber of {}: {}'.format(i,elem.count(i)))
        print('Percentage of {}: {}%'.format(i,elem.perc(i)))
    print('\n')
