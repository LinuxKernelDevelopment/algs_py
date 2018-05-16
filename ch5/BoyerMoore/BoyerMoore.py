#!/home/hmsjwzb/python/bin/python3

import sys

class BoyerMoore:
    R = None
    right = None

    pattern = None

    def __init__(self, pat):
        self.R = 256
        self.pat = pat
    
        self.right = [-1] * self.R

        for j in range(0, len(pat)):
            self.right[ord(pat[j])] = j

    def search(self, txt):
        m = len(pat)
        n = len(txt)
        i = 0
        while i <= n - m:
            skip = 0
            for j in range(m-1, -1, -1):
                if pat[j] != txt[i+j]:
                    skip = max(1, j - self.right[ord(txt[i+j])])
                    break
            if skip == 0:
                return i
            i += skip
        return n

if __name__ == '__main__':
    pat = sys.argv[1]
    txt = sys.argv[2]

    boyermoore1 = BoyerMoore(pat)
    offset1 = boyermoore1.search(txt)

    print("text:    " + str(txt))

    o_str = "pattern: "
    for i in range(0, offset1):
        o_str += " "
    o_str += pat
    print(o_str)

