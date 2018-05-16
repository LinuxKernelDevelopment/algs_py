#!/home/hmsjwzb/python/bin/python3
import sys

class RabinKarp:
    def __init__(self, pat):
        self.pat = pat
        self.R = 256
        self.m = len(pat)
        self.q = self.longRandomPrime()

        self.RM = 1
        for i in range(1, self.m):
            self.RM = (self.R * self.RM) % self.q
        self.patHash = self.hash(pat, self.m)

    def hash(self, key, m):
        h = 0
        for j in range(0, m):
            h = (self.R * h + ord(key[j])) % self.q
        return h

    def check(self, txt, i):
        for j in range(0, self.m):
            if self.pat[j] != txt[i+j]:
                return False
        return True

    def search(self, txt):
        n = len(txt)
        if n < self.m:
            return n
        txtHash = self.hash(txt, self.m)

        if self.patHash == txtHash and self.check(txt, 0):
            return 0

        for i in range(self.m, n):
            txtHash = (txtHash + self.q - self.RM*ord(txt[i-self.m]) % self.q) % self.q
            txtHash = (txtHash*self.R + ord(txt[i])) % self.q

            offset = i - self.m + 1
            if self.patHash == txtHash and self.check(txt, offset):
                return offset
        return n

    def longRandomPrime(self):
        return 541

if __name__ == '__main__':
    pat = sys.argv[1]
    txt = sys.argv[2]

    searcher = RabinKarp(pat)
    offset = searcher.search(txt)

    print("text:    " + str(txt))

    mystr = "pattern: "
    for i in range(0, offset):
        mystr += " "
    mystr += pat
    print(mystr)

