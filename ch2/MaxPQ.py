#!/home/hmsjwzb/python/bin/python3
from StdIn import StdIn

class MaxPQ:
    def __init__(self, maxN):
        self.pq = [None] * (maxN+1)
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, v):
        if self.N >= len(self.pq) - 1:
            self.pq.extend([None] * len(self.pq))
        self.N += 1
        self.pq[self.N] = v
        self.swim(self.N)

    def swim(self, k):
        while k > 1 and self.pq[k//2] < self.pq[k]:
            self.exch(k//2, k)
            k = k // 2

    def sink(self, k):
        while k*2 <= self.N:
            j = 2 * k
            if j < self.N and self.pq[j] < self.pq[j+1]: j += 1
            if not self.pq[k] < self.pq[j]:
                break
            self.exch(k, j)
            k = j

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def delMax(self):
        if self.isEmpty():
            raise Exception("Priority queue underflow")
        max = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.sink(1)
        self.pq[self.N + 1] = None
        if self.N > 0 and self.N == (len(self.pq) - 1) / 4:
            self.pq = self.pq[0:len(self.pq)/2]
        return max

if __name__ == '__main__':
    pq = MaxPQ(1)
    StdIn = StdIn()
    while not StdIn.isEmpty():
        item = StdIn.readString()
        if not item == "-":
            pq.insert(item)
        elif not pq.isEmpty():
            print(pq.delMax() + " ")

    print("(" + str(pq.size()) + " left on pq)")
