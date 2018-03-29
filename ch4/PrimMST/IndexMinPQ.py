#!/home/hmsjwzb/python/bin/python3.5

class IndexMinPQ:
    def __init__(self, maxN):
        if maxN < 0:
            raise OverflowError()
        self.maxN = maxN
        self.n = 0
        self.keys = [None] * (maxN + 1)
        self.pq = [None] * (maxN + 1)
        self.qp = [None] * (maxN + 1)
        for i in range(0, maxN+1):
            self.qp[i] = -1

    def isEmpty(self):
        return self.n == 0

    def contains(self, i):
        if i < 0 or i >= self.maxN:
            raise OverflowError()
        return self.qp[i] != -1

    def size(self):
        return self.n

    def insert(self, i, key):
        if i < 0 or i >= self.maxN:
            raise OverflowError()
        if self.contains(i):
            raise OverflowError('index is already in priority queue')
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        #print(self.n)
        self.keys[i] = key
        self.swim(self.n)

    def minIndex(self):
        if self.n == 0:
            raise OverflowError('Priority queue underflow')
        return self.keys[self.pq[1]]

    def minKey(self):
        if self.n == 0:
            raise OverflowError('Priority queue underflow')
        return self.keys[self.pq[1]]

    def delMin(self):
        if self.n == 0:
            raise OverflowError('Priority queue underflow')
        min = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        assert(min == self.pq[self.n+1])
        self.qp[min] = -1
        self.keys[min] = None
        self.pq[self.n+1] = -1
        return min

    def KeyOf(self, i):
        if i < 0 or i >= self.maxN:
            raise OverflowError()
        if not self.contains(i):
            raise OverflowError('index is not in the priority queue')
        return self.keys[i]

    def changeKey(self, i, key):
        if i < 0 or i >= self.maxN:
            raise OverflowError()
        if not self.contains(i):
            raise OverflowError('index is not in the priority queue')
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def change(self, i, key):
        self.changeKey(i, key)

    def decreaseKey(self, i, key):
        if i < 0 or i >= self.maxN:
            raise OverflowError()
        if not self.contains(i):
            raise OverflowError('index is not in the priority queue')
        if self.keys[i] < key:
            raise OverflowError('Calling increaseKey() with given argument would not strictly increase the key')
        self.keys[i] = key
        self.sink(self.qp[i])

    def delete(self, i):
        if i < 0 or i >= self.maxN:
            raise OverflowError()
        if not self.contains(i):
            raise OverflowError('index is not in the priority queue')
        self.exch(index, n)
        self.n -= 1
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1

    def greater(self, i, j):
        #print(self.keys[self.pq[i]], self.keys[self.pq[j]])
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swim(self, k):
        while k > 1 and self.greater(k//2, k):
            self.exch(k, k//2)
            k = k//2

    def sink(self, k):
        while 2*k <= self.n:
            j = 2 * k
            if j < self.n and self.greater(j, j+1):
                j += 1
            if not self.greater(k, j): break
            self.exch(k, j)
            k = j

    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        try:
            result = self.pq[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

if __name__ == '__main__':
    strings = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst' ];
    pq = IndexMinPQ(len(strings))
    for i in range(0, len(strings)):
        pq.insert(i, strings[i])

    while not pq.isEmpty():
        i = pq.delMin()
        print("%d %s" % (i, strings[i]))
    print('\n')

    for i in range(0, len(strings)):
        pq.insert(i, strings[i])

    for i in pq:
        print("%d %s" % (i, strings[i]))
    while not pq.isEmpty():
        pq.delMin()
