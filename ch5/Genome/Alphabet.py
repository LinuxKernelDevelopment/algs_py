#!/usr/bin/python
import sys
class Alphabet:
    ''''DNA = Alphabet("ACGT")
    DECIMAL = Alphabet("0123456789")'''
    def __init__(self, arg1):
        if type(arg1) is int:
            self.Alphabet_int(arg1)
        elif type(arg1) is str:
            self.Alphabet_str(arg1)
        elif type(arg1) is  None:
            self.Alphabet_int(256)

    def Alphabet_int(self, radix):
        self.R = radix
        self.alphabet = [None] * self.R
        self.inverse = [None] * self.R

        for i in range(0, self.R):
            self.aphabet[i] = chr(i)
        for i in range(0, self.R):
            self.inverse[i] = i

    def Alphabet_str(self, alpha):
        unicode = [False] * sys.maxunicode
        for i in range(0, len(alpha)):
            c = alpha[i]
            if unicode[ord(c)]:
                raise ValueError('Illegal alphabet: repeated character = %c' % (c))
            unicode[ord(c)] = True

        self.alphabet = alpha
        self.R = len(alpha)
        self.inverse = [0] * sys.maxunicode
        for i in range(0, len(self.inverse)):
            self.inverse[i] = -1

        for c in range(0, self.R):
            self.inverse[ord(self.alphabet[c])] = c

    def contains(self, c):
        return self.inverse[c] != -1

    def R(self):
        return self.R

    def radix(self, R):
        return self.R

    def lgR(self):
        lgR = 0
        t = self.R - 1
        while t >= 1:
            lgR += 1
            t /= 2
        return lgR

    def toIndex(self, c):
        if ord(c) >= len(self.inverse) or self.inverse[ord(c)] == -1:
            raise ValueError("Character %c not in alphabet" % (c))
        return self.inverse[ord(c)]


    def toIndices(self, s):
        source = s
        target = [0] * len(s)
        for i in range(0, len(source)):
            target[i] = self.toIndex(source[i])
        return target

    def toChar(self, index):
        if index < 0 or index >= self.R:
            raise ValueError("index must be between 0 and %d:%d" % (self.R, index))
        return self.alphabet[index]

    def toChars(self, indices):
        s = ""
        for i in range(0, len(indices)):
            s += self.toChar(indices[i])
        return s

class ALPHABET:
    BASE64 = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    DNA = Alphabet("ACGT")
    DECIMAL = Alphabet("0123456789")

if __name__ == '__main__':
    tmp = ALPHABET()

    encoded1 = tmp.BASE64.toIndices("NowIsTheTimeForAllGoodMen")
    decoded1 = tmp.BASE64.toChars(encoded1)
    print(decoded1)

    encoded2 = tmp.DNA.toIndices("AACGAACGGTTTACCCCG")
    decoded2 = tmp.DNA.toChars(encoded2)
    print(decoded2)

    encoded3 = tmp.DECIMAL.toIndices("01234567890")
    decoded3 = tmp.DECIMAL.toChars(encoded2)
    print(decoded3)
