#!/home/hmsjwzb/python/bin/python3

class stack:
    def __init__(self):
        self.a = [None]
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def resize(self, max):
        temp = [None] * max
        for i in range(0, self.N):
            temp[i] = self.a[i]
        self.a = temp

    def push(self, item):
        if self.N == len(self.a):
            self.resize(2 * len(self.a))
        self.a[self.N] = item
        self.N = self.N + 1
        #print('N++' + str(self.N))

    def pop(self):
        self.N = self.N - 1
        #print('N--' + str(self.N))
        item = self.a[self.N]
        if self.N > 0 and self.N == len(self.a)/4:
            self.resize(len(self.a)//2)
        return item

    def iterator(self):
        for i in range(len(self.a), 1, -1):
            yield self.a[i]


