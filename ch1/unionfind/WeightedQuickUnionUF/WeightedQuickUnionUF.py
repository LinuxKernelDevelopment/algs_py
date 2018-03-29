#!/home/hmsjwzb/python/bin/python3

class WeightedQuickUnionUF:
    def __init__(self, n):
        self.count = n
        self.id = [None] * n
        self.sz = [None] * n
        for i in range(n):
            self.id[i] = i
            self.sz[i] = 1

    def count_components(self):
        return self.count

    def find(self, p):
        self.validate(p)
        while p != self.id[p]:
            p = self.id[p]
        return p

    def count(self):
        return self.count

    def validate(self, p):
        n = len(self.id)
        if p < 0 and p >= n:
            raise IndexError

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.id[p] == self.id[q]

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.sz[rootP] > self.sz[rootQ]:
            self.id[rootP] = rootQ; self.sz[rootQ] += self.sz[rootP]
        else:
            self.id[rootQ] = rootP; self.sz[rootP] += self.sz[rootQ]
        self.count -= 1
