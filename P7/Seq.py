class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # this method is called every time a new object is created

        self.strbases = strbases

    def len(self):
        return str(len(self.strbases))

    def complement(self):
        seq = self.strbases
        seq = seq.upper()
        for index, elem in enumerate(seq):
            if elem == 'A':
                seq = seq[:index] + seq[index:].replace('A', 'T')
            if elem == 'T':
                seq = seq[:index] + seq[index:].replace('T', 'A')
            if elem == 'C':
                seq = seq[:index] + seq[index:].replace('C', 'G')
            if elem == 'G':
                seq = seq[:index] + seq[index:].replace('G', 'C')
        return seq

    def reverse(self):
        seq = self.strbases.upper()[::-1]
        return seq

    def count(self, base):
        base=base.upper()
        return str(self.strbases.upper().count(base))

    def perc(self, base):
        seq = self.strbases.upper()
        base=base.upper()
        counter= seq.count(base)
        tl = len(seq)
        return str(round(100.0 * counter/tl, 2))