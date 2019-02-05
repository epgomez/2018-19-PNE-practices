class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # this method is called every time a new object is created


        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq class
    All the objects of Gene class will inherit the
    methods from the Seq class"""
    pass


s1 = Gene('ATTCTGTGC')
s2 = Seq('AACCTTAACCGG')

print(s1)
print(s2)

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2: int = s2.len()

print('Sequence 1: {}'.format(str1))
print('Lenght1 is: {}'.format(l1))
print('Sequence 2: {}'.format(str2))
print('Lenght2 is: {}'.format(l2))

print('end')
