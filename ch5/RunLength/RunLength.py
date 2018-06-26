#!/usr/bin/python
import os
import sys
from BinaryStdIn import BinaryStdIn
from BinaryStdOut import BinaryStdOut

class RunLength:
    R = 256
    LG_R = 8

    def __init__(self):
        self.BinaryStdIn = BinaryStdIn()
        self.BinaryStdOut = BinaryStdOut()
        pass

    def expand(self):
        b = False
        while not self.BinaryStdIn.isEmpty():
            run = self.BinaryStdIn.readInt_r(self.LG_R)
            for i in range(0, run):
                self.BinaryStdOut.write_b(b)
            b = not b
        self.BinaryStdOut.close()

    def compress(self):
        run = 0
        old = False
        while not self.BinaryStdIn.isEmpty():
            b = self.BinaryStdIn.readBoolean()
            if b != old:
                self.BinaryStdOut.write_i_r(run, self.LG_R)
                run = 1
                old = not old
            else:
                if run == self.R - 1:
                    self.BinaryStdOut.write_i_r(run, self.LG_R)
                    run = 0
                    self.BinaryStdOut.write_i_r(run, self.LG_R)
                run += 1
        self.BinaryStdOut.write_i_r(run, self.LG_R)
        self.BinaryStdOut.close()

if __name__ == '__main__':
    Rl = RunLength()
    if sys.argv[1] == '-':
        Rl.compress()
    elif sys.argv[1] == '+':
        Rl.expand()
