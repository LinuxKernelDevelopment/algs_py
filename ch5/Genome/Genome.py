#!/usr/bin/python
from Alphabet import ALPHABET
import sys

class Genome:
    def __init__(self):
        pass

    def compress(self):
        myin = open('/dev/stdin', 'r')
        myout = open('/dev/stdout', 'w')
        DNA = ALPHABET.DNA
        s = myin.buffer.read()
        n = len(s)
        #print(str(n), str(n.to_bytes(8, sys.byteorder)))
        myout.buffer.write(n.to_bytes(8, sys.byteorder))

        for i in range(0, n):
            d = DNA.toIndex(chr(s[i]))
            myout.buffer.write(d.to_bytes(2, sys.byteorder))

    def expand(self):
        myin = open('/dev/stdin', 'r')
        myout = open('/dev/stdout', 'w')
        DNA = ALPHABET.DNA
        n = int.from_bytes(myin.buffer.read(8), byteorder=sys.byteorder)
        print(n)
        for i in range(0, n):
            c = int.from_bytes(myin.buffer.read(2), byteorder=sys.byteorder)
            myout.write(DNA.toChar(c))


if __name__ == '__main__':
    G = Genome()
    if sys.argv[1] == '-':
        G.compress()
    elif sys.argv[1] == '+':
        G.expand()
