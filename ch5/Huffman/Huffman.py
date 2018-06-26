#!/usr/bin/python

from BinaryStdIn import BinaryStdIn
from BinaryStdOut import BinaryStdOut
import sys
from MinPQ import MinPQ

class Node:
    def __init__(self, ch, freq, left, right):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def isLeaf(self):
        assert ((self.left == None) and (self.right == None)) or ((self.left != None ) and (self.right != None))
        return (self.left == None ) and (self.right == None)

    def compareTo(self, that):
        return self.freq - that.freq

    def __lt__(self, that):
        return self.freq < that.freq


class Huffman:
    R = 256

    def __init__(self):
        self.Bin = BinaryStdIn()
        self.Bout = BinaryStdOut()

    def compress(self):
        s = self.Bin.readString()

        freq = [0] * self.R
        for i in range(0, len(s)):
            freq[ord(s[i])] += 1

        root = self.buildTrie(freq)

        st = [None] * self.R
        self.buildCode(st, root, "")

        self.writeTrie(root)

        self.Bout.write_i(len(s))

        for i in range(0, len(s)):
            code = st[ord(s[i])]
            for j in range(0, len(code)):
                if code[j] == '0':
                    self.Bout.write_b(False)
                elif code[j] == '1':
                    self.Bout.write_b(True)
                else:
                    raise ValueError("Illegal state")

        self.Bout.close()

    def buildTrie(self, freq):
        pq = MinPQ()
        for i in range(0, self.R):
            if freq[i] > 0:
                pq.insert(Node(i, freq[i], None, None))

        if pq.size() == 1:
            if freq['\0'] == 0:
                pq.insert(Node('\0', 0, None, None))
            else:
                pq.insert(Node('\1', 0, None, None))

        while pq.size() > 1:
            left = pq.delMin()
            right = pq.delMin()
            parent = Node('\0', left.freq + right.freq, left, right)
            pq.insert(parent)

        return pq.delMin()

    def writeTrie(self, x):
        if x.isLeaf():
            self.Bout.write_b(True)
            self.Bout.write_i_r(x.ch, 8)
            return
        self.Bout.write_b(False)
        self.writeTrie(x.left)
        self.writeTrie(x.right)

    def buildCode(self, st, x, s):
        if not x.isLeaf():
            self.buildCode(st, x.left, s + '0')
            self.buildCode(st, x.right, s + '1')
        else:
            st[x.ch] = s

    def expand(self):
        root = self.readTrie()

        length = self.Bin.readInt()

        for i in range(0, length):
            x = root
            while not x.isLeaf():
                bit = self.Bin.readBoolean()
                if bit:
                    x = x.right
                else:
                    x = x.left
            self.Bout.write_i(x.ch)
        self.Bout.close()

    def readTrie(self):
        isLeaf = self.Bin.readBoolean()
        if isLeaf:
            return Node(self.Bin.readChar(), -1, None, None)
        else:
            return Node('\0', -1, self.readTrie(), self.readTrie())

if __name__ == '__main__':
    huf = Huffman()
    if sys.argv[1] == '-':
        huf.compress()
    elif sys.argv[1] == '+':
        huf.expand()
    else:
        raise ValueError("Illegal command line argument")


