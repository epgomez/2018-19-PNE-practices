def count(seq):
    """Counting the number of As in the string"""

    resulta: int = 0
    resultc = 0
    resultt = 0
    resultg = 0
    seq=seq.upper()
    for b in seq:
        if b == 'A':
            resulta += 1
        if b == 'C':
            resultc += 1
        if b == 'T':
            resultt += 1
        if b == 'G':
            resultg += 1

    return resulta, resultc, resultt, resultg


def perc(seq):
    """Calculating lenght and percentages"""
    tl= len(seq)
    a,c,t,g=count(seq)
    list=[a, c, t, g]
    per_a, per_c, per_t, per_t=0,0,0,0
    list_per=[per_a, per_c, per_t, per_t]
    for i, elem in zip(list, range(4)):
        list_per[elem]=round(100.0 * i/tl, 1)
    return list_per


def main():
    seq = input('Enter your sequence: ')
    lenght= len(seq)
    a, c, t, g = count(seq)
    bases = ['A','C','T','G']
    list = [a, c, t, g]
    list_perc = perc(seq)
    print('This sequence is of lenght {}'.format(lenght))
    for elem, per, i in zip (list, list_perc, bases):
        print ('Base {}\n   Counter: {}\n   Percentage: {}'.format(i,elem,per))


def main_2():
    seq1 = input('Enter your first sequence: ')
    seq2 = input('Enter your second sequence: ')
    sequences=[seq1, seq2]
    order=['first', 'second']

    for i, number in zip(sequences, order):
        lenght= len(i)
        a, c, t, g = count(i)
        bases = ['A','C','T','G']
        list = [a, c, t, g]
        list_perc = perc(i)

        print('\nThe {} sequence is of lenght {}\n'.format(number, lenght))

        for elem, per, i in zip (list, list_perc, bases):
            print ('Base {}\n   Counter: {}\n   Percentage: {}'.format(i,elem,per))