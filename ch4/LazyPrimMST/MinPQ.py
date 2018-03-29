#!/home/hmsjwzb/python/bin/python3.5
from StdIn import StdIn

class MinPQ:
    def __init__(self, initCapacity=None, keys=None):
        if initCapacity == None and keys == None:
            self.MinPQ_initCapacity(1)
        elif keys != None:
            self.MinPQ_keys(keys)

    def MinPQ_initCapacity(self, initCapacity):
        self.pq = [None] * (initCapacity + 1)
        self.n = 0

    def MinPQ_keys(self, keys):
        self.n = len(keys)
        self.pq = [None] * (len(keys) + 1)
        for i in range(1, n):
            self.pq[i+1] = keys[i]
        for k in range(n//2, 0):
            self.sink(k)
        assert(self.isMinHeap())

    def isEmpty(self):
        return self.n == 0

    def size(self):
        return self.n

    def min(self):
        if self.isEmpty():
            raise OverflowError("Priority queue underflow")
        return self.pq[1]

    def resize(self, capacity):
        assert(capacity > self.n)
        temp = [None] * capacity
        for i in range(1, self.n+1):
            temp[i] = self.pq[i]
        self.pq = temp

    def insert(self, x):
        if self.n == len(self.pq) - 1:
            self.resize(2 * len(self.pq))
        self.n += 1
        self.pq[self.n] = x
        self.swim(self.n)

    def delMin(self):
        if self.isEmpty():
            raise OverflowError("Priority queue underflow")
        min = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        self.pq[self.n+1] = None
        if self.n > 0 and (self.n == (len(self.pq) - 1) // 4):
            self.resize(len(self.pq) // 2)
        return min

    def swim(self, k):
        while k > 1 and self.greater(k//2, k):
            self.exch(k, k//2)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.greater(j, j+1):
                j+= 1
            self.exch(k, j)
            k = j

    def greater(self, i, j):
        return self.pq[i] > self.pq[j]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def IsMinHeap(self):
        return self.isMinHeap(1)

    def isMinHeap(self, k):
        if k > self.n: return True
        left = 2 * k
        right = 2*k + 1
        if left <= n and self.greater(k, left): return False
        if right <= n and self.greater(k, right): return False
        return self.isMinHeap(left) and isMinHeap(right)

if __name__ == '__main__':
    pq = MinPQ()
    myin = StdIn()
    s = ""
    while not myin.isEmpty():
        item = myin.readString()
        if not item == '-':
            pq.insert(item)
        elif not pq.isEmpty():
            s += str(pq.delMin()) + " "
    print(s + "(" + str(pq.size()) + " left on pq)")
