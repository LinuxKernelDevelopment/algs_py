#!/home/hmsjwzb/python/bin/python3

from Mystr import MyStr
from StdIn import StdIn
import sys
sys.path.append("/home/hmsjwzb/Algorithm/ch3/SequentialSearchST")
from SequentialSearchST import SequentialSearchST

class SeparateChainingHashST:
    def __init__(self, m):
        self.m = m
        self.n = 0
        self.st = [None] * m
        for i in range(0, self.m):
            self.st[i] = SequentialSearchST()

    def resize(self, chains):
        temp = SeparateChainingHashST(chains)
        for i in range(0, self.m):
            for key in st[i].keys():
                temp.put(key, st[i].get(key))
        self.m = temp.m
        self.n = temp.n
        self.st = temp.st
        
    def hash(self, key):
        return (key.hashCode() & 0x7fffffff) % self.m

    def size(self):
        return self.n

    def contains(self, key):
        if key == None:
            raise Error("argument to contains() is null")
        return self.get(key) != None

    def get(self, key):
        if key == None:
            raise Error("argument to contains() is null")
        i = self.hash(key)
        return self.st[i].get(key)

    def put(self, key, val):
        if key == None:
            raise Error("argument to contains() is null")
        if val == None:
            self.delete(key)
            return

        if self.n >= 10 * self.m: self.resize(2 * self.m)

        i = self.hash(key)
        if not self.st[i].contains(key): self.n += 1
        self.st[i].put(key, val)

    def delete(self, key):
        if key == None:
            raise Error("argument to contains() is null")
        
        i = self.hash(key)
        if st[i].contains(key): self.n -= 1
        st[i].delete(key)

        if self.m > 4 and self.n <= 2 * self.m:
            self.resize(self.m / 2)

    def keys(self):
        for i in range(0, self.m):
            for key in self.st[i].keys():
                yield key

if __name__ == '__main__':
    st = SeparateChainingHashST(997)
    i = 0
    In = StdIn()
    while not In.isEmpty():
        key = In.readString()
        st.put(MyStr(key), i)
        i += 1

    for s in st.keys():
        print("%s %d" % (s.Str, st.get(s)))
