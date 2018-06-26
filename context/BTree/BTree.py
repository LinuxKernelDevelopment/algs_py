#!/usr/bin/python

class Node:
    def __init__(self, k):
        self.m = k
        self.children = [None] * 4

class Entry:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class BTree:
    M = 4
    height = 0
    n = 0

    def __init__(self):
        self.root = Node(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.n

    def height_m(self):
        return self.height

    def get(self, key):
        if key == None:
            raise ValueError("argument to get() is None")
        return self.search(self.root, key, self.height)

    def search(self, x, key, ht):
        children = x.children

        if ht == 0:
            for j in range(0, x.m):
                print(key)
                print(children[j].key)
                print("\n")
                if key == children[j].key:
                    return children[j].val
        else:
            for j in range(0, x.m):
                if j+1 == x.m or key < children[j+1].key:
                    print(key)
                    print(children[j].key)
                    print(children[j].val)
                    return self.search(children[j].next, key, ht-1)
        return None

    def put(self, key, val):
        if key == None:
            raise ValueError("argument key to put() is null")
        u = self.insert(self.root, key, val, self.height)
        self.n += 1
        if u == None:
            return

        t = Node(2)
        t.children[0] = Entry(self.root.children[0].key, None, self.root)
        t.children[1] = Entry(u.children[0].key, None, u)
        self.root = t
        self.height += 1

    def insert(self, h, key, val, ht):
        t = Entry(key, val, None)
        m = 0
        if ht == 0:
            for j in range(0, h.m):
                print(key + "\t" + h.children[j].key + "\t" + str(key < h.children[j].key))
                if key < h.children[j].key:
                    break
        else:
            for j in range(0, h.m):
                if j+1 == h.m or key < h.children[j+1].key:
                    u = self.insert(h.children[j].next, key, val, ht-1)
                    m = j + 1
                    if u == None:
                        return None
                    t.key = u.children[0].key
                    t.next = u
                    break
        for i in range(h.m, m, -1):
            h.children[i] = h.children[i-1]
        h.children[m] = t
        h.m += 1
        if h.m < self.M:
            return None
        else:
            return self.split(h)

    def split(self, h):
        t = Node(self.M // 2)
        h.m = self.M // 2
        for j in range(0, self.M//2):
            t.children[j] = h.children[self.M//2+j]
        return t

    def toString(self):
        return self.toString_r(self.root, self.height, "") + "\n"

    def toString_r(self, h, ht, indent):
        s = ""
        children = h.children

        if ht == 0:
            for j in range(0, h.m):
                s += "\t" + children[j].key + " " + children[j].val + '\n'
        else:
            for j in range(0, h.m):
                if j > 0:
                    s += (indent + "(" + children[j].key + ")\n")
                s += (self.toString_r(children[j].next, ht-1, indent + "     "))
        return s

    def __str__(self):
        return self.toString()


if __name__ == '__main__':
    st = BTree()

    st.put("www.cs.princeton.edu", "128.112.136.12")
    st.put("www.cs.princeton.edu", "128.112.136.11")
    st.put("www.princeton.edu", "128.112.128.15")
    st.put("www.yale.edu", "130.132.143.21")
    st.put("www.simpsons.com", "209.052.165.60")
    st.put("www.apple.com", "17.112.152.32")
    st.put("www.amazon.com", "207.171.182.16")
    st.put("www.ebay.com", "66.135.192.87")
    st.put("www.cnn.com", "64.236.16.20")
    st.put("www.google.com", "216.239.41.99")
    st.put("www.nytimes.com", "199.239.136.200")
    st.put("www.microsoft.com", "207.126.99.140")
    st.put("www.dell.com", "143.166.224.230")
    st.put("www.slashdot.org", "66.35.250.151")
    st.put("www.espn.com", "199.181.135.201")
    st.put("www.weather.com", "63.111.66.11")
    st.put("www.yahoo.com", "216.109.118.65")

    print(st)
    print("cs.princeton.edu " + st.get("www.cs.princeton.edu"))

    print("size:    %d" % (st.size()))
    print("height:  %d" % (st.height_m()))
    print(st)

