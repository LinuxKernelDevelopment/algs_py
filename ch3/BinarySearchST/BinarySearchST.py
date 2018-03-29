#!/home/hmsjwzb/python/bin/python3

from StdIn import StdIn

class BinarySearchST:
    def __init__(self):
        capacity = 2
        self.keys = [None] * capacity
        self.vals = [None] * capacity
        self.n = 0

    def size(self):
        return self.n

    def isEmpty(self):
        return self.size() == 0

    def get(self, key):
        if self.isEmpty():
            return None
        i = self.rank(key)
        if i < self.n and self.keys[i] == key:
            return self.vals[i]
        else:
            return None

    def put(self, key, val):
        i = self.rank(key)
        if i < self.n and self.keys[i] == key:
            self.vals[i] = val
            return None
        if self.n == len(self.keys):
            self.resize(2 * len(self.keys))
        for j in range(self.n, i-1, -1):
            self.keys[j] = self.keys[j-1]
            self.vals[j] = self.vals[j-1]
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def rank(self, key):
        lo = 0 
        hi = self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def min(self):
        return self.keys[0]

    def max(self):
        return self.keys[self.N-1]

    def select(self, k):
        return self.keys[k]

    def ceiling(self, key):
        i = self.rank(key)
        return self.keys[i]

    def Keys(self, lo, hi):
        for i in self.keys[0:self.n]:
            yield i

    def delete(self, key):
        if self.isEmpty():
            return None
        i = self.rank(key)
        if i == self.n or self.keys[i] != key:
            return None
        for j in range(i, n-1):
            self.keys[j] = self.keys[j+1]
            self.vals[j] = self.vals[j+1]
        self.n-=1
        self.keys[n] = None
        self.vals[n] = None
        if self.n > 0 and self.n == len(self.keys)/4:
            self.resize(len(self.keys)/2)

    def resize(self, capacity):
        tempk = [None] * capacity
        tempv = [None] * capacity
        for i in range(0, self.n):
            tempk[i] = self.keys[i]
            tempv[i] = self.vals[i]
        self.vals = tempv
        self.keys = tempk

    def contains(self, key):
        return self.get(key) != None

if __name__ == '__main__':
    st = BinarySearchST(2)
    StdIn = StdIn()
    i = 0
    while not StdIn.isEmpty():
        key = StdIn.readString()
        st.put(key, i)
        i += 1
    for s in st.Keys(0, st.size()):
        print(s + " " + str(st.get(s)))
