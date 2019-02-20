def letters(ms):
    ms = ms.upper()
    if (ms.strip('ACTG')==''):
        return False
    else:
        return True

print(letters('actggtgtgagagagtgtatagatacgagatgc'))