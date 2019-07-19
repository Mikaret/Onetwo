import stdio
import sys


def isValid(dna):
    DNA = ['A', 'C', 'T', 'G']
    for i in range(len(dna)):
        if dna[i] not in DNA:
            return False
    if 'A' not in dna:
        return False
    elif 'C' not in dna:
        return False
    elif 'G' not in dna:
        return False
    elif 'T' not in dna:
        return False
    else:
        return True


def _main():
    dna = sys.argv[1]
    stdio.writeln(isValid(dna.upper()))

if __name__ == '__main__':
    _main()
