#!/home/hmsjwzb/python/bin/python3

from Mystr import MyStr
from StdIn import StdIn

class LinearProbingHashST:
    def __init__(self, capacity):
        self.m = capacity
        self.n = 0
        self.keys = [None] * self.m
        self.vals = [None] * self.m

    def size(self):
        return self.n

    def isEmpty(self):
        return self.size() == 0

    def contains(self, key):
        if key == None:
            raise Exception("argument to contains() is null")
        return self.get(key) != None

    def hash(self, key):
        return (key.hashCode() & 0x7fffffff) % self.m

    def resize(self, capacity):
        temp = LinearProbingHashST(capacity)
        for i in range(0, m):
            if self.keys[i] != None:
                temp.put(self.keys[i], self.vals[i])
        self.keys = temp.keys
        self.vals = temp.vals
        self.m = temp.m

    def put(self, key, val):
        if key == None:
            raise Exception("first argument to put() is None")
        if val == None:
            self.delete(key)
            return

        if self.n >= self.m / 2:
            self.resize(2 * self.m)

        i = self.hash(key)
        while self.keys[i]:
            if self.keys[i].equals(key):
                self.val[i] = val
                return
            i = (i + 1) % self.m
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def get(self, key):
        if key == None:
            raise Exception("argument to get() is null")
        i = self.hash(key)
        while self.keys[i].equals(key):
            return self.vals[i]
        return None

    def delete(self, key):
        if key == None:
            raise Exception("argument to delete() is null")
        if not self.contains(key):
            return

        i = self.hash(key)
        while not key.equals(self.keys[i]):
            i = (i + 1) % m

        self.keys[i] = None
        self.vals[i] = None

        i = (i + 1) % m
        while self.keys[i] != None:
            keyToRehash = self.keys[i]
            valToRehash = self.vals[i]
            self.keys[i] = None
            self.vals[i] = None
            self.n -= 1
            self.put(keyToRehash, valToRehash)
            i = (i + 1) % m

        self.n -= 1

        if self.n > 0 and self.n <= self.m / 8:
            self.resize(self.m / 2)

    def Keys(self):
        for i in range(0, self.m):
            key = self.keys[i]
            yield key


if __name__ == '__main__':
    st = LinearProbingHashST(4)
    i = 0
    In = StdIn()
    while not In.isEmpty():
        key = In.readString()
        st.put(MyStr(key), i)
        i += 1

    for s in st.Keys():
        if s:
            print("%s %s" % (s.Str, st.get(s)))
