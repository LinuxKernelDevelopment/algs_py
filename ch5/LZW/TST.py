#!/usr/bin/python
import sys
sys.path.append("/home/hmsjwzb/algs/algs_py/tools")
from In import In
import time
import pdb

class Node:
    def __init__(self):
        self.c = None
        self.left = None
        self.mid = None
        self.right = None
        self.val = None

class TST:
    def __init__(self):
        self.n = 0
        self.root = None

    def size(self):
        return self.n

    def contains(self, key):
        if key == None:
            raise ValueError("argument to contains() is null")
        return self.get(key) != None

    def get(self, key):
        if key == None:
            raise ValueError("key must have length >= 1")
        x = self.get_r(self.root, key, 0)
        if x == None:
            return None
        return x.val

    def get_r(self, x, key, d):
        if x == None:
            return None
        if len(key) == 0:
            raise ValueError("key must have length >= 1")
        c = key[d]
        if c < x.c :
            return self.get_r(x.left, key, d)
        elif c > x.c:
            return self.get_r(x.right, key, d)
        elif d < len(key) - 1:
            return self.get_r(x.mid, key, d+1)
        else:
            return x

    def put(self, key, val):
        if key == None:
            raise ValueError("calls put() with null key")
        if not self.contains(key):
            self.n += 1
        self.root = self.put_r(self.root, key, val, 0)

    def put_r(self, x, key, val, d):
        c = key[d]
        if x == None:
            x = Node()
            x.c = c
        if c < x.c:
            x.left = self.put_r(x.left, key, val, d)
        elif c > x.c:
            x.right = self.put_r(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self.put_r(x.mid, key, val, d+1)
        else:
            x.val = val
        return x

    def longestPrefixOf(self, query):
        if query == None:
            raise ValueError("calls longestPrefixOf() with null argument")
        if len(query) == 0:
            return None
        length = 0
        x = self.root
        i = 0
        while x != None and i < len(query):
            c = query[i]
            if c < x.c:
                x = x.left
            elif c > x.c:
                x = x.right
            else:
                i += 1
                if x.val != None:
                    length = i
                x = x.mid
        return query[0:length]

    def keys(self):
        queue = []
        prefix = ""
        self.collect(self.root, prefix, queue)
        return queue

    def keysWithPrefix(self, prefix):
        if prefix == None:
            raise ValueError("calls keysWithPrefix() with null argument")
        queue = []
        x = self.get_r(self.root, prefix, 0)
        if x == None:
            return queue
        if x.val != None:
            queue += [prefix]
        self.collect(x.mid, prefix, queue)
        return queue

    def collect(self, x, prefix, queue):
        if x == None:
            return
        self.collect(x.left, prefix, queue)
        if x.val != None:
            queue += [prefix + x.c]
        prefix += x.c
        self.collect(x.mid, prefix, queue)
        prefix = prefix[:-1]
        self.collect(x.right, prefix, queue)

    def keysThatMatch(self, pattern):
        prefix = ""
        queue = []
        self.collect_p(self.root, prefix, 0, pattern, queue)
        return queue

    def collect_p(self, x, prefix, i, pattern, queue):
        if x == None:
            return
        c = pattern[i]
        if c == '.' or c < x.c:
            self.collect_p(x.left, prefix, i, pattern, queue)
        if c == '.' or c == x.c:
            if i == len(pattern) - 1 and x.val != None:
                queue += [prefix + x.c]
            prefix += x.c
            self.collect_p(x.mid, prefix, i+1, pattern, queue)
            prefix = prefix[0:-1]
        if c == '.' or c > x.c:
            self.collect_p(x.right, prefix, i, pattern, queue)

if __name__ == '__main__':
    myin = In("/home/hmsjwzb/algs/algs_py/ch5/TST/shellsST.txt", None)
    st = TST()
    i = 0
    for key in myin:
        print("put " + str(key) + " " + str(i))
        st.put(key, i)
        i += 1
    if st.size() < 100:
        print("keys(\"\")")
        for key in st.keys():
            print(str(key) + " " + str(st.get(key)))
        print("\n")

    print("longestPrefixOf(\"shellsort\"):")
    print(st.longestPrefixOf("shellsort"))
    print("\n")

    print("longestPrefixOf(\"shell\"):")
    print(st.longestPrefixOf("shell"))
    print("\n")

    print("keysWithPrefix(\"shor\"):")
    for s in st.keysWithPrefix("shor"):
        print(s)
    print("\n")

    print("KeysThatMatch(\".he.l.\"):")
    for s in st.keysThatMatch(".he.l."):
        print(s)

