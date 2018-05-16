#!/home/hmsjwzb/python/bin/python3
import sys

class KMP:
    R = 0
    dfa = None

    pattern = None
    pat = None

    def __init__(self, pat):
        self.R = 256
        self.pat = pat

        m = len(pat)
        self.dfa = [[0 for j in range(m)] for i in range(self.R)]
        self.dfa[ord(pat[0])][0] = 0
        x = 0
        for j in range(0, m):
            for c in range(0, self.R):
                self.dfa[c][j] = self.dfa[c][x]
            self.dfa[ord(pat[j])][j] = j + 1
            x = self.dfa[ord(pat[j])][x]


    def search(self, txt):
        m = len(self.pat)
        n = len(txt)
        i = 0
        j = 0
        while i < n and j < m:
            j = self.dfa[ord(txt[i])][j]
            i += 1
        if j == m:
            return i - m
        return n

if __name__ == '__main__':
    pat = sys.argv[1]
    txt = sys.argv[2]

    kmp1 = KMP(pat)
    offset1 = kmp1.search(txt)

    print("text:    " + txt)
    
    out_str = "pattern: "
    for i in range(0, offset1):
        out_str += " "
    out_str += pat
    print(out_str)
