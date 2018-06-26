#!/usr/bin/python
from BinaryStdIn import BinaryStdIn
from BinaryStdOut import BinaryStdOut
import sys
from TST import TST

class LZW:
    R = 256
    L = 4096
    W = 12

    def __init__(self):
        self.Bin = BinaryStdIn()
        self.Bout = BinaryStdOut()
        pass

    def compress(self):
        input = self.Bin.readString()
        st = TST()
        for i in range(0, self.R):
            st.put("" + chr(i), i)
        code = self.R + 1

        while len(input) > 0:
            s = st.longestPrefixOf(input)
            self.Bout.write_i_r(st.get(s), 12)
            t = len(s)
            if t < len(input) and code < self.L:
                st.put(input[0:t+1], code)
                code += 1
            input = input[t:]
        self.Bout.write_i_r(self.R, self.W)
        self.Bout.close()

    def expand(self):
        st = [" "] * self.L
        for i in range(0, self.R):
            st[i] = "" + chr(i)
        st[i] = ""
        i += 1

        codeword = self.Bin.readInt_r(self.W)
        if codeword == self.R:
            return

        val = st[codeword]

        while True:
            #print(val, file=sys.stderr)
            self.Bout.write_S(val)
            codeword = self.Bin.readInt_r(self.W)
            if codeword == self.R:
                break
            s = st[codeword]
            if i == codeword:
                s = val + val[0]
            if i < self.L:
                st[i] = val + s[0]
                i += 1
            #print(st,file=sys.stderr)
            val = s
        self.Bout.close()

if __name__ == '__main__':
    lzw = LZW()
    if sys.argv[1] == '-':
        lzw.compress()
    elif sys.argv[1] == '+':
        lzw.expand()

