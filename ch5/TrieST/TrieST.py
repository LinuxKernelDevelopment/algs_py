#!/home/hmsjwzb/python/bin/python3
import sys
sys.path.append("/home/hmsjwzb/intel/Algorithm/tools/")
from In import In
import time
import pdb

R = 256
class TrieST:
    class Node:
        def __init__(self):
            self.val = None
            self.next = [None] * R

        def __str__(self):
            retstr = ""
            retstr += ("val:" + str(self.val) + "\n" + "next:")
            retstr += (str(self.next) + "\t")
            retstr += "\n"
            return retstr

        def __repr__(self):
            retstr = ""
            retstr += ("val:" + str(self.val) + "\n" + "next:")
            for item in self.next:
                retstr += (str(item) + "\t")
            retstr += "\n"
            return retstr

    def __init__(self):
        self.root = None
        self.n = 0

    def get(self, key):
        if key == None:
            raise ValueError("argument to get() is null")
        x = self.get_r(self.root, key, 0)
        if x == None:
            return None
        return x.val

    def contains(self, key):
        if key == None:
            raise ValueError("argument to contains() to null")
        return self.get(key) != None

    def get_r(self, x, key, d):
        if x == None:
            return None
        if d == len(key):
            return x
        c = self.charAt(key, d)
        return self.get_r(x.next[ord(c)], key, d+1)

    def put(self, key, val):
        if key == None:
            raise ValueError("first argument to put() is null")
        if val == None:
            self.delete(key)
            return
        else:
            self.root = self.put_r(self.root, key, val, 0)
            

    def put_r(self, x, key, val, d):
        if x == None:
            x = self.Node()
            #print(x)
        if d == len(key):
            if x.val == None:
                self.n += 1
            x.val = val
            return x
        #print(key)
        #print(d)
        c = self.charAt(key, d)
        #print(c)
        #print(ord(c))
        #pdb.set_trace()
        x.next[ord(c)] = self.put_r(x.next[ord(c)], key, val, d+1)
        return x

    def charAt(self, key, d):
        return key[d]

    def size(self):
        return self.n

    def isEmpty(self):
        return self.size() == 0

    def keys(self):
        return self.keysWithPrefix("")

    def keysWithPrefix(self, prefix):
        #print(self.root)
        results = []
        #pdb.set_trace()
        x = self.get_r(self.root, prefix, 0)
        self.collect(x, prefix, results)
        return results

    def collect(self, x, prefix, results):
        if x == None:
            return
        if x.val != None:
            results += [prefix]
        for c in range(0, R):
            prefix += chr(c)
            #print(prefix)
            #print(x.next[c])
            self.collect(x.next[c], prefix, results)
            prefix = prefix[0:len(prefix)-1]

    def keysThatMatch(self, pattern):
        results = []
        estr = ""
        self.collect_p(self.root, estr, pattern, results)
        return results

    def collect_p(self, x, prefix, pattern, results):
        if x == None:
            return
        d = len(prefix)
        if d == len(pattern) and x.val != None:
            results += [prefix]
        if d == len(pattern):
            return
        c = self.charAt(pattern, d)
        if c == '.':
            for ch in range(0, R):
                prefix += chr(ch)
                self.collect_p(x.next[ch], prefix, pattern, results)
                prefix = prefix[:-1]
        else:
            prefix += c
            self.collect_p(x.next[ord(c)], prefix, pattern, results)
            prefix = prefix[:-1]

    def longestPrefixOf(self, query):
        if query == None:
            raise ValueError("argument to longestPrefixOf is None")
        length = self.longestPrefixOf_r(self.root, query, 0, -1)
        if length == -1:
            return None
        else:
            return query[0:length]

    def longestPrefixOf_r(self, x, query, d, length):
        if x == None:
            return length
        if x.val != None:
            length = d
        if d == len(query):
            return length
        c = self.charAt(query, d)
        return self.longestPrefixOf_r(x.next[ord(c)], query, d+1, length)

    def delete(self, key):
        if key == None:
            raise ValueError("argument to delete() is None")
        self.root = self.delete_r(self.root, key, 0)

    def delete_r(self, x, key, d):
        if x == None:
            return None
        if d == len(key):
            if x.val != None:
                self.n -= 1
                x.val = None
        else:
            c = self.charAt(key, d)
            x.next[c] = self.delete(x.next[c], key, d+1)

        if x.val != None:
            return x
        for c in range(0, R):
            if x.next[c] != None:
                return x
        return None

    def __str__(self):
        self.print_root(self.root, 1)

    def print_root(self, x, d):
        if x == None:
            return
        str = ""
        str += '\t' * d
        str += x.val
        print(str)
        for item in x.next:
            self.print_root(item, d+1)

if __name__ == '__main__':
    myin = In("/home/hmsjwzb/intel/Algorithm/ch5/TrieST/shellsST.txt", None)
    st = TrieST()
    i = 0
    for key in myin:
        st.put(key, i)
        i += 1
    print(st.size())
    if st.size() < 100:
        print("keys(\"\"):")
        for key in st.keys():
            print(str(key) + " " + str(st.get(key)))
        print("\n")
    print("longestPrefixOf(\"shellsort\"):")
    print(st.longestPrefixOf("shellsort"))
    print("\n")

    print("longestPrefixOf(\"quicksort\"):")
    print(st.longestPrefixOf("quicksort"))
    print("\n")

    print("keysWithPrefox(\"shor\"):")
    for s in st.keysWithPrefix("shor"):
        print(s)
    print("\n")

    print("keysThatMatch(\".he.l.\"):")
    for s in st.keysThatMatch(".he.l."):
        print(s)
